# Tuples
# Implement a function that takes a tuple of strings as input and returns a new tuple 
# containing only the strings that start with an uppercase letter.

def filter_uppercase_strings(strings):
    # Your code here
    new_string=()
    for i in strings:
        if i[0].isupper():
          new_string += (i,)
    return new_string
# Test the function
strings = ("Apple", "banana", "Cat", "dog", "Elephant", "Frog")
print(filter_uppercase_strings(strings))  # Expected output: ("Apple", "Cat", "Elephant")
