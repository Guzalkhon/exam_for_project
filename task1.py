def transform_days():
    days = int(input('Enter days: '))

    years = days // 365
    days %= 365
    print(f'Years: {years}')

    monthes = days // 30
    days %= 30
    print(f'Monthes: {monthes}')

    weeks = days // 7
    days %= 7
    print(f'Weeks: {weeks}')
    print(f'Days: {days}')

transform_days()