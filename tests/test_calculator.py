import pytest
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

class TestAdd:
    def test_add_positive_numbers(self, calc):
        assert calc.add(2, 3) == 5
    
    def test_add_negative_numbers(self, calc):
        assert calc.add(-2, -3) == -5
    
    def test_add_mixed_numbers(self, calc):
        assert calc.add(-5, 10) == 5
    
    def test_add_with_zero(self, calc):
        assert calc.add(0, 5) == 5
        assert calc.add(5, 0) == 5
    
    def test_add_floats(self, calc):
        assert calc.add(2.5, 3.7) == pytest.approx(6.2)


class TestSubtract:
    def test_subtract_positive_numbers(self, calc):
        assert calc.subtract(10, 3) == 7
    
    def test_subtract_negative_numbers(self, calc):
        assert calc.subtract(-5, -3) == -2
    
    def test_subtract_mixed_numbers(self, calc):
        assert calc.subtract(5, 10) == -5
    
    def test_subtract_with_zero(self, calc):
        assert calc.subtract(10, 0) == 10
        assert calc.subtract(0, 10) == -10
    
    def test_subtract_floats(self, calc):
        assert calc.subtract(5.5, 2.3) == pytest.approx(3.2)


class TestMultiply:
    def test_multiply_positive_numbers(self, calc):
        assert calc.multiply(4, 5) == 20
    
    def test_multiply_negative_numbers(self, calc):
        assert calc.multiply(-3, -4) == 12
    
    def test_multiply_mixed_numbers(self, calc):
        assert calc.multiply(-5, 4) == -20
    
    def test_multiply_with_zero(self, calc):
        assert calc.multiply(0, 5) == 0
        assert calc.multiply(10, 0) == 0
    
    def test_multiply_floats(self, calc):
        assert calc.multiply(2.5, 4) == 10.0


class TestDivide:
    def test_divide_positive_numbers(self, calc):
        assert calc.divide(10, 2) == 5
    
    def test_divide_negative_numbers(self, calc):
        assert calc.divide(-10, -2) == 5
    
    def test_divide_mixed_numbers(self, calc):
        assert calc.divide(-10, 2) == -5
        assert calc.divide(10, -2) == -5
    
    def test_divide_floats(self, calc):
        assert calc.divide(7.5, 2.5) == pytest.approx(3.0)
    
    def test_divide_by_zero_raises_error(self, calc):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc.divide(10, 0)
    
    def test_divide_zero_by_number(self, calc):
        assert calc.divide(0, 5) == 0
