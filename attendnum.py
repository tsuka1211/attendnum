from datetime import datetime, timedelta
from collections import Counter

# 日付と同じ出席番号を当てるパターン
def same_as_date(date):
    return int(date.strftime("%d"))

# 日付と月の数字を全部足すパターン
def sum_of_digits(date):
    day_month = date.strftime("%d%m")
    return sum(int(digit) for digit in day_month) % max_attendance

# 日付と月を足すパターン
def sum_of_date_and_month(date):
    day = int(date.strftime("%d"))
    month = int(date.strftime("%m"))
    return (day + month) % max_attendance

# 日付と月をそのまま合わせるパターン
def concatenate_date_and_month(date):
    day_month = date.strftime("%d%m")
    return int(day_month) % max_attendance

def main():
    global max_attendance
    max_attendance = int(input("出席番号の最大値を入力してください: "))

    # 2024年の範囲で土日と長期休暇を除外して日付を取得
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 12, 31)
    business_days = list(get_business_days(start_date, end_date))

    patterns = [
        ("Same as date", same_as_date),
        ("Sum of digits", sum_of_digits),
        ("Sum of date and month", sum_of_date_and_month),
        ("Concatenate date and month", concatenate_date_and_month)
    ]

    # 出席番号のカウンターを初期化
    attendance_counter = Counter()

    for date in business_days:
        for pattern_name, pattern_func in patterns:
            attendance_counter[pattern_func(date)] += 1

    # 出現回数でソートし、トップ3を取得
    top_3_attendance = attendance_counter.most_common(3)
    print("Top 3 most common attendance numbers throughout the business days in the year:")
    for i, (attendance, count) in enumerate(top_3_attendance, start=1):
        print(f"{i}. 一番当てられやすい番号は: {attendance}番, 当てられる予想回数は: {count}回です")

# 土日と長期休暇を除外して日付を取得
def get_business_days(start_date, end_date):
    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() < 5:  # 0:月曜日, 1:火曜日, ..., 4:金曜日
            if not ((current_date.month == 3 and 15 <= current_date.day <= 31) or
                    (current_date.month == 4 and 1 <= current_date.day <= 2) or
                    (current_date.month == 7 and 25 <= current_date.day) or
                    (current_date.month == 8 and current_date.day <= 31) or
                    (current_date.month == 12 and 23 <= current_date.day) or
                    (current_date.month == 1 and current_date.day <= 7)):
                yield current_date
        current_date += timedelta(days=1)

if __name__ == "__main__":
    main()
