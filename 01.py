from datetime import datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    birthdays_per_week = defaultdict(list)
    today = datetime.today().date()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=7)
    
    for user in users:
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days
        birthday_weekday = (today + timedelta(days=delta_days)).strftime("%A")
        
        if birthday_weekday in ['Saturday', 'Sunday']:
            birthday_weekday = 'Monday'

        if start_of_week <= birthday_this_year < end_of_week:
            birthdays_per_week[birthday_weekday].append(user["name"])

    for day, names in birthdays_per_week.items():
        if names:
            print(f"{day}: {', '.join(names)}")


users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Steve Jobs", "birthday": datetime(1955, 2, 24)},
    {"name": "Mark Zuckerberg", "birthday": datetime(1984, 5, 14)}
]

get_birthdays_per_week(users)
