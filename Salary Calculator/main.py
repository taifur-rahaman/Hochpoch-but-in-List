# Salary Calculator

userName = input("Enter Your Name: ")
userID = input("Enter Your ID: ")
hourly_wages = float(input("Enter Your Hourly Wages: "))

day_week = ["monday", "tuesday", "wednesday", "thrusday", "friday"]
hour_day = []

for i in range(0, 5):
    hour_day.append(int(input(f"Enter the working hour on {day_week[i].title()}: ")))

weekly_salary = sum(hour * hourly_wages for hour in hour_day)

print(f"Name : {userName}\nID: {userID}\nYou have Work total of {sum(hour_day)} hour this week\nTotal Payment: {weekly_salary}\n")