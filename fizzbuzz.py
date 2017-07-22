# a first foray into pytest
def fizzbuzz(x):
    if (x > 21):
        return "er, you should have stopped!"
    elif (x == 21):
        return "drink!"
    elif ((x % 3) == 0 and (x % 5) == 0):
        return "fizzbuzz"
    elif (x % 3) == 0:
        return "fizz"
    elif (x % 5) == 0:
        return "buzz"
    else:
        return x + 1

class TestClass(object):
    def test_number(self):
        assert fizzbuzz(1) == 2

    def test_fizz(self):
        assert fizzbuzz(3) == "fizz"

    def test_buzz(self):
        assert fizzbuzz(10) == "buzz"

    def test_fizzbuzz(self):
        assert fizzbuzz(15) == "fizzbuzz"

    def test_twentyone(self):
        assert fizzbuzz(21) == "drink!"

    def test_overrun(self):
        assert fizzbuzz(22) == "er, you should have stopped!"
