from app.fizzbuzz import calculate


def test_calculate_input_of_three_returns_fizz():
    value = calculate(3)

    assert "Fizz" == value

def test_calculate_input_of_five_returns_buzz():
    value = calculate(5)

    assert "Buzz" == value

def test_calculate_input_of_multiple_of_three_and_five():
    value = calculate(15)

    assert "FizzBuzz" == value