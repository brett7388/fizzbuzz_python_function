from app.fizzbuzz import calculate


def test_calculate_input_of_three_returns_fizz():
    value = calculate(3)

    assert "Fizz" == value

def test_calculate_input_of_five_returns_buzz():
    value = calculate(5)

    assert "Buzz" == value

def test_calculate_input_of_three_and_five_returns_fizzbuzz():
    value = calculate(15)

    assert "FizzBuzz" == value

def test_caluclate_divisble_of_one():
    value = calculate(1)

    assert 1 == value

def test_calculate_divisble_of_three():
    value = calculate(6)

    assert "Fizz" == value

def test_calculate_divisble_of_five():
    value = calculate(10)

    assert "Buzz" == value

def test_calculate_divisble_of_30():
    value = calculate(30)

    assert "FizzBuzz" == value