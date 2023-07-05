# Project 1: Currency converter in Python

# with open('currency_rates.txt') as f:
#     lines = f.readlines()

# currencyDict = {}

# for line in lines:
#     parsed = line.split('\t')
#     currencyDict[parsed[0]] = parsed[2]

# print(currencyDict)
# amount = int(input('Enter the amount: '))
# [print(item) for item in currencyDict.keys()]
# currency = input('Enter the currency to be converted to in available options: ')
# print(f'{amount} INR is equal to {amount * float(currencyDict[currency])} {currency}')

# Project 2: HTTP server for web development
# open the folder where your html file is present and open powershell in this folder
# python -m http.server --bind=localhost
# OR 
# python -m http.server
# this creates a server in the localhost:8000

# Project 3: reminder
# import time
# from plyer import notification

# while True:
#     notification.notify(
#         title = "Please Drink Water",
#         message = "Else you will be sick",
#         # app_icon = ".ico file"
#         timeout = 5
# )
#     time.sleep(60*60) # reminder every hour

    # to run python in the background: run pythonw .\main.py

# Project 4: Password Generator
import string
import random

s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.digits
s4 = string.punctuation
plen = int(input('Enter the password length: '))
s = []
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))

random.shuffle(s)
print("".join(s[0:plen]))
