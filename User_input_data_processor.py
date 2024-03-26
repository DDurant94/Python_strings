'''
2. User Input Data Processor
Objective:
The aim of this assignment is to process and format user input data.

Task 1: Input Length Validator
Write a script that checks the length of the user's first name and last name. Both should be at least 2 characters long. 
If not, print an error message.

Task 2: Password Complexity Checker
Create a function that checks the complexity of a user's password. The password must be at least 8 characters long, 
contain one uppercase letter, one lowercase letter, and one number. If the password does not meet these criteria, 
print a message explaining the complexity requirements.

Task 3: Email Formatter
Implement a script that ensures all user email addresses are in a standard format
'''

# Task one


def user_checker(first_name,last_name):
  if len(first_name) < 3:
    return "Error first name is not long enough."
  elif len(last_name) < 3:
    return "Error last name is not long enough."
  else:
    return f"{str.capitalize(first_name)} {str.capitalize(last_name)} meet requirements."


while True:
  user_choice = input("Do you want to start? [Y/N] ").upper()
  if user_choice == "Y":
    first_name = input("Enter in your first name: ")
    last_name = input("Enter in your last name: ")
    print(user_checker(first_name, last_name))
  elif user_choice == "N":
    break
  else:
    print("invalid input!")


# Task two

import re

def password_checker(password):
  if len(password) < 8:
    return "Password must be at least 8 characters long."
#      looking for upper case letters 
  if not re.search(r'[A-Z]', password):
    return "Password needs at least one uppercase letter in it."
#          looking for lower case letters
  if not re.search(r'[a-z]', password):
    return "Password needs at least one lowercase letter in it."
#          looking for a number in password
  if not re.search(r'[0-9]', password):
    return "Password must contain at least one number in it."


  return "Password meets complexity requirement."
        


password = str(input("Please enter in your password: "))
print((password_checker(password)))

# Task three  
import re 


def email_checker(user_email):  # allows specials (.(any)) have to close with \ on the . and - but not the _
#        check against     email user has  @(only one) company . com/net/org
  pattern = re.compile(r"^[a-zA-z0-9\.\-_]+@{1}[a-zA-Z0-9]+\.{1}[a-zA-Z]{2,3}$")
  if pattern.search(user_email) == None:
    return f"{user_email} can not be validated."
  else:
    return f"{user_email} was validated."
    
      

user_email = str(input("Enter your email in please: "))
print(email_checker(user_email))