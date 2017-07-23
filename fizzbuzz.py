# a first foray into pytest
def fizzbuzz(x):
    nextnumber = x + 1
    if (x > 21):
        return "er, you should have stopped!"
    elif (nextnumber == 21):
        return "drink!"
    elif ((nextnumber % 3) == 0 and (nextnumber % 5) == 0):
        return "fizzbuzz"
    elif (nextnumber % 3) == 0:
        return "fizz"
    elif (nextnumber % 5) == 0:
        return "buzz"
    else:
        return nextnumber

class TestClass(object):
    def test_number1(self):
        assert fizzbuzz(1) == 2

    def test_number6(self):
        assert fizzbuzz(6) == 7

    def test_fizz(self):
        assert fizzbuzz(2) == "fizz"

    def test_buzz(self):
        assert fizzbuzz(9) == "buzz"

    def test_fizzbuzz(self):
        assert fizzbuzz(14) == "fizzbuzz"

    def test_twentyone(self):
        assert fizzbuzz(20) == "drink!"

    def test_overrun(self):
        assert fizzbuzz(22) == "er, you should have stopped!"
