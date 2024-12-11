# Fizz_Buzz_game_example_itertools
import itertools as its

def fizz_buzz(n):
    fizzes = its.cycle([""] * 2 + ["Fizz"])
    buzzes = its.cycle([""] * 4 + ["Buzz"])  # Fixing the cycle length for Buzz
    fizzes_buzzes = (fizz + buzz for fizz, buzz in zip(fizzes, buzzes))
    result = (word or num for word, num in zip(fizzes_buzzes, its.count(1)))
    for i in its.islice(result, n):  # Limit results to 'n' terms
        print(i)

# Run the function
fizz_buzz(100) # If you need to chance n just change the number in the function fizz_buzz
