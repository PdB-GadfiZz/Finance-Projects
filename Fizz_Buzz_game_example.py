# Fizz Buzz game example

def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0: 
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input

for i in range(1, 101):
    print(fizz_buzz(i))

