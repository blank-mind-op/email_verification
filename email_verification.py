import regex as re

email_regex = re.compile(r'^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$')

user_email = input("Enter your email : ")


try:
    verification = email_regex.search(user_email)
    print(verification.group())
    print("You entered a legetimate email addresse!!!")
except AttributeError:
    print("This is not a valid email addresse //")