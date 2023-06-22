# Write a function that checks whether a given number num is a prime number.
# A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers.
#
# RETURNS a boolean

def is_prime_number(num):

    # TODO: Check if num is a prime number
    # num>1
    # if int(num/num) == 1 & int(num/1)==num:
    #     return True

    for i in range(2,num):
        if (num%1)==0:
            return True
# Test the function
num = int(input("Enter a number: "))
is_prime = is_prime_number(num)
if is_prime:
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
