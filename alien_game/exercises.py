# Write a function that returns the max of two numbers #
# n1 = input("give me a number: ")
# n2 = input("give me another number: ")

def max(n1, n2):
    if n1 > n2:
        print(n1)
    elif n1 < n2:
        print(n2)
    else:
        print("The numbers are the same!")

max(n1,n2)

#################################################

# Write a function called fizz_buzz that takes a number #
# If the number is divisible by 3, return "Fizz" #
# If the number is divisible by 5, return "Buzz" #
# If divisible by both 3 and 5, return "FizzBuzz" #
# If not divisible by either, return the number #
num = input("Give fizzbuzz a number: ")
def fizz_buzz(n):
    if int(n) % 3 == 0 and int(n) % 5 == 0:
        return "FizzBuzz"
    elif int(n) % 3 == 0:
        return "Fizz"
    elif int(n) % 5 == 0:
        return "Buzz"
    else:
        return int(n)

print(fizz_buzz(num))

#################################################

# Write a function called showNumbers that takes parameter limit
# Should print all numbers between 0 and limit with a label to identify even and odd
lim = input("Give me a limit: ")

def showNumbers(n):
    for i in range(int(n)):
        if 

