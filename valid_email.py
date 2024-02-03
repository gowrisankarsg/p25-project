import re

def is_valid_email(email):
    # Regular expression for a basic email validation
    pattern = re.compile(r"[^@\s]+@[^@\s]+\.[a-zA-Z]+$")
    return pattern.match(email)

def get_valid_email():
    while True:
        email = input("Please enter your email: ")
        if is_valid_email(email):
            return email
        else:
            print("Invalid email. Please enter a valid email.")

# Example usage
valid_email = get_valid_email()
print("You entered a valid email:", valid_email)
