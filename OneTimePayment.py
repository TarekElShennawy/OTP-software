#E-mail One-Time Payment (OTP) System for verification by Tarek ElShennawy.
import os
import math
import random
import smtplib

digits="1234567890" #Put digits in a string to concatenate them in a loop

for digit in range(5):
    otpcode+=digits[math.floor(random.random() * 10)]

otpmessage = otpcode + " is your generated OTP."

#Initialising connection between program and Gmail using SMTP
smtpconnect = smtplib.SMTP('smtp.gmail.com', 587)
smtpconnect.starttls()
smtpconnect.login("G-mail", "Relevant App Password")

useremail = input("Your Email: ")
s.sendmail('&&&&&&&&&&&&', useremail, otpmessage)
otpinput = input("Enter your OTP :")
if otpinput == otpcode:
    print("Correct. You  may enter.")
else:
    print("Incorrect. Please retry your OTP code.")
