
import pytest
from app.calculator import Calculator

class TestCalc:

    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_good(self):
        assert self.calc.multiply(self, 2, 2)

    def test_division_calculate_good(self):
        assert  self.calc.division(self, 6, 2)

    def test_subtraction_calculate_good(self):
        assert  self.calc.subtraction(self, 5, 2)

    def test_zero_division(self):
            with pytest.raises(ZeroDivisionError):
                self.calc.division(self, 1, 0)

    def teardown(self):
        print('Выполнение метода TearDown')


