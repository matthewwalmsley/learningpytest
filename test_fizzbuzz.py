# a first foray into pytest
import fizzbzz.py

class TestClass(object):
    def test_number(self):
        assert fizzbuzz(1) == 2
