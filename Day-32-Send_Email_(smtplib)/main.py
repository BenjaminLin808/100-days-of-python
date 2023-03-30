# import smtplib


# my_email = "benjaminlin808@gmail.com"
# password = "dtmmfwrfkjbqaofp"

# # connection = smtplib.SMTP("smtp.gmail.com", 587)
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="benjaminlin808@yahoo.com", msg="Subject:Hello\n\nThis is the body of the email.")
# # connection.close()


import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

date_of_birthday = dt.datetime(year=2001, month=3, day=15)
print(date_of_birthday)