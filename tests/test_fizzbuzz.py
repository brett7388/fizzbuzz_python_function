from app.fizzbuzz import calculate


def test_calculate_input_of_three_returns_fizz():
    value = calculate(3)

    assert "Fizz" == value

def test_calculate_input_of_five_returns_buzz():
    value = calculate(5)

    assert "Buzz" == value

def test_calculate_input_of_three_and_five():
    value = calculate(15)

    assert "FizzBuzz" == value

def test_calculate_input_of_none():
    value = calculate(1)

    assert 1 == value

def test_calculate_input_of_six():
    value = calculate(6)

    assert "Fizz" == value

def test_calculate_input_of_ten():
    value = calculate(10)

    assert "Buzz" == value

def test_calculate_input_of_30():
    value = calculate(30)

    assert "FizzBuzz" == value

def test_caluclate_input_of_two():
    value = calculate(2)

    assert 2 == value