#Monday Motivation Project
import smtplib
import datetime as dt
import random

MY_EMAIL = "benjaminlin808@gmail.com"
MY_PASSWORD = "dtmmfwrfkjbqaofp"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="benjamin808@yahoo.com",
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )





