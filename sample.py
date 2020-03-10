def Fizzbuzz(number):
    if number % 5 == 0 and number % 3 == 0:
        return "Fizbuzz"
    elif number % 5 == 0:
        return "Buzz"
    elif number % 3 == 0:
        return "Fizz"
    else:
        return number


if __name__ == "__main__":
    print(Fizzbuzz(6))  # Fizz
    print(Fizzbuzz(15))  # FizzBuzz
    print(Fizzbuzz(10))  # Buzz
    print(Fizzbuzz(7))  # Number
