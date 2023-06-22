# Write a function to calculate the factorial of a given number (n).
# hint: try recursion

def factorial(n):
   f=1
   for i in range(1, n+1):
      f=f*i
      print(f)
   return f



# Test case
number = 5
result = factorial(number)
print(f"The factorial of {number} is: {result}")

