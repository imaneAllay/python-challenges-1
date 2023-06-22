# Exercise 2: Conditional Statements
# TODO: Write code that checks if a number (num) is positive, negative, or zero using if-else statements

def main():
    number = input (" enter a number: ")
    number = int(number)
    # If positive, print "The number is positive"
    if number >0:
        print("positive")
    # If negative, print "The number is negative"
    elif number < 0 :
        print("Negative")
    # If zero, print "The number is zero"
    elif number == 0:
        print ("The number is zero")
    else:
        print("Invalide input")





main()