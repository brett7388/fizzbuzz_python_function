
def calculate(number):
    if number % 15 ==0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number == 5:
        return "Buzz"
    
    else:
        return 1
