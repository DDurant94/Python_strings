'''
3. Interactive Help Desk Bot
Objective:
The aim of this assignment is to create an interactive help desk bot that processes user queries
 and responds appropriately for a SaaS application.

Task 1: Command Parser
Write a script that takes a user's text input and identifies if it contains one of the
 predefined commands (e.g., "help", "issue", "contact support"). If a command is found, print a response related to the command.

Task 2: Issue Categorizer
If the user's input contains the word "issue", further categorize the issue based on keywords such as 
"login", "performance", "error", etc. Print out the category of the issue for the support team.
'''
# Task one

user_input = input("What do you need? ")
#                for key (help)  value (answer after the :) i need to use .items() to unpack them
predefined_commands = {"help": "Sure thing here is the help information I have on that", "issue": "Thank you for reporting this big to us!", "contact support": "Here is the number for our support team 1-888-888-8888."}
for key, value in predefined_commands.items():
  result = user_input.find(key)
  if result == -1:
    pass
  else:
    print(value)

# Task two
    


def help_desk(user_input):
  help_commands = {"billing": "Let me connect you to someone for our billing department.", "shipping": "Let me connect you with someone about shipping."}
  predefined_commands = {"help": "Sure thing here is the help information I have.", "issue": "Thank you for reporting this big to us!", "contact support": "Here is the number for our support team 1-888-888-8888."}
  for key, value in predefined_commands.items():
    result = user_input.find(key)
    # i need to check result for a -1 first or it wont work 
    if result == -1:
      pass
    elif key == "help":
      print(value)
      print("1. Shipping\n2. Billing")
      user_help = str(input("Enter your answer please: ")).lower()
      for hc_key, value1 in help_commands.items():
        result2 = user_help.find(hc_key)
        if result2 == -1:
          pass
        elif hc_key == "billing":
          print(value1)
        elif hc_key == "shipping":
          print(value1)
        else:
          print("invalid input.")
    elif key == "issue":
      print(value)


    elif key == "contact support":
      print(value)



user_input = input("What is can we do for you? ")
help_desk(user_input)