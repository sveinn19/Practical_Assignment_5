def Fizzbuzz(number):
    if number % 5 == 0 and number % 3 == 0:
        return "Fizbuzz"
    elif number % 5 == 0:
        return "Buzz"
    elif number % 3 == 0:
        return "Fizz"
    else:
        return number


print(Fizzbuzz(6))
print(Fizzbuzz(15))
print(Fizzbuzz(10))
print(Fizzbuzz(7))
