# Exercise 3: Loops
# TODO: Write code that prints all between 1 and n using a while loop
# TODO: Write code that prints all the even numbers between 1 and n using a for loop

def main(n):
    print("All numbers from 1 to n:")
    # use a while loop

    # while n>0:
    #     print(n)
    #     n-=1



    print("Even numbers between 1 and n:")
    # even numbers from 1-n (for loop)
    for x in range(1, n+1):
        if x%2 ==0:
            print(x)



main(12)