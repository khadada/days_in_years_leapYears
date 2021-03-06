def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is leap year")
                return True
            else:
                return False
        else:
            print(f"{year} is leap year")
            return True
    else:
        return False


def days_in_month(year, month):
    # this 2 lines [if statement]  below are debugging for invalid number of month
    if month < 1 or month > 12:
        return f"{month} is invalid number"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year):
        month_days[1] = 29

    return month_days[month]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: ")) - 1
days = days_in_month(year, month)
print(days)












