# Write a function that takes a password as input and checks its strength based on the following criteria:
#
# At least 8 characters long
# Contains both uppercase and lowercase letters
# Includes at least one digit
#
# The function should RETURN a boolean value indicating whether the password meets the criteria.

def check_password_strength(password):
    is_strong = True
    # TODO: Implement the password strength checking logic
    if (len(password)<=8):
        print('At least 8 characters long')
        is_strong = False
    if not any(c.isupper() for c in password):
        print('Password should have at least one uppercase letter')
        is_strong = False
    if not any(c.islower() for c in password):
        print("Password should have at least one lowercase letter")
        is_strong = False
    if not any(c.isdigit() for c in password):
        print('Includes at least one digit')
        is_strong = False


    return is_strong



# Test the function
password = input("Enter a password: ")
is_strong = check_password_strength(password)
print("Is the password strong?", is_strong)

