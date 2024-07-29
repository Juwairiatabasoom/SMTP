##################### Extra Hard Starting Project ######################
import random,os,pandas as pd
import datetime as dt
import smtplib
MY_EMAIL="ohmymamamia69@gmail.com"
password="ekyi rsmc cxjj fwwf"
# 1. Update the birthdays.csv
now=dt.datetime.now()
data=pd.read_csv("birthdays.csv")
for key,value in data.iterrows():
    if (value.month) == now.month and (value.day)== now.day:

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        file_path=f"letter_templates/letter_{random.randint(1,3)}.txt"
        with open(file_path) as letter:
            content = letter.read()
            birthday_letter=content.replace("[NAME]",f"{(value["name"])}")

# 4. Send the letter generated in step 3 to that person's email address.

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL,password=password)
            connection.sendmail(from_addr=MY_EMAIL,to_addrs=f"{value["email"]}",msg=f"Subject:Birthday Wishes\n\n{birthday_letter}")



