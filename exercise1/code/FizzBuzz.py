def it_FizzorBuzz(numbers):
    if numbers % 3 and numbers % 5 == 0:
        return "FizzBuzz"
    elif numbers % 3 == 0:
        return "Fizz"
    elif numbers % 5 == 0:
        return "Buzz"