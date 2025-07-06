"""
Unit tests for the calculator module.
"""

import pytest
from src.calculator import Calculator, add, subtract, multiply, divide


class TestCalculator:
    """Test cases for the Calculator class."""

    def setup_method(self):
        """Set up a fresh calculator instance for each test."""
        self.calc = Calculator()

    def test_add(self):
        """Test addition operation."""
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(-1, 1) == 0
        assert self.calc.add(0.5, 0.5) == 1.0
        assert self.calc.add(0, 0) == 0

    def test_subtract(self):
        """Test subtraction operation."""
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(1, 1) == 0
        assert self.calc.subtract(0, 5) == -5
        assert self.calc.subtract(10.5, 5.5) == 5.0

    def test_multiply(self):
        """Test multiplication operation."""
        assert self.calc.multiply(2, 3) == 6
        assert self.calc.multiply(0, 5) == 0
        assert self.calc.multiply(-2, 3) == -6
        assert self.calc.multiply(2.5, 2) == 5.0

    def test_divide(self):
        """Test division operation."""
        assert self.calc.divide(6, 2) == 3
        assert self.calc.divide(5, 2) == 2.5
        assert self.calc.divide(0, 5) == 0
        assert self.calc.divide(-6, 2) == -3

    def test_divide_by_zero(self):
        """Test division by zero returns None."""
        assert self.calc.divide(5, 0) is None

    def test_power(self):
        """Test power operation."""
        assert self.calc.power(2, 3) == 8
        assert self.calc.power(5, 0) == 1
        assert self.calc.power(2, -1) == 0.5
        assert self.calc.power(0, 5) == 0

    def test_history(self):
        """Test calculation history functionality."""
        # Perform some calculations
        self.calc.add(1, 2)
        self.calc.multiply(3, 4)
        self.calc.divide(10, 2)

        history = self.calc.get_history()
        assert len(history) == 3
        assert "1 + 2 = 3" in history[0]
        assert "3 * 4 = 12" in history[1]
        assert "10 / 2 = 5.0" in history[2]

    def test_clear_history(self):
        """Test clearing calculation history."""
        self.calc.add(1, 2)
        self.calc.multiply(3, 4)

        assert len(self.calc.get_history()) == 2

        self.calc.clear_history()
        assert len(self.calc.get_history()) == 0


class TestCalculatorFunctions:
    """Test cases for the standalone calculator functions."""

    def test_add_function(self):
        """Test add function."""
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
        assert add(0.5, 0.5) == 1.0

    def test_subtract_function(self):
        """Test subtract function."""
        assert subtract(5, 3) == 2
        assert subtract(1, 1) == 0
        assert subtract(0, 5) == -5

    def test_multiply_function(self):
        """Test multiply function."""
        assert multiply(2, 3) == 6
        assert multiply(0, 5) == 0
        assert multiply(-2, 3) == -6

    def test_divide_function(self):
        """Test divide function."""
        assert divide(6, 2) == 3
        assert divide(5, 2) == 2.5
        assert divide(0, 5) == 0

    def test_divide_function_by_zero(self):
        """Test divide function with zero divisor."""
        assert divide(5, 0) is None


class TestCalculatorEdgeCases:
    """Test edge cases and error conditions."""

    def setup_method(self):
        """Set up a fresh calculator instance for each test."""
        self.calc = Calculator()

    def test_large_numbers(self):
        """Test operations with large numbers."""
        large_num = 999999999
        assert self.calc.add(large_num, 1) == large_num + 1
        assert self.calc.multiply(large_num, 2) == large_num * 2

    def test_floating_point_precision(self):
        """Test floating point arithmetic precision."""
        result = self.calc.add(0.1, 0.2)
        assert abs(result - 0.3) < 1e-10

    def test_negative_numbers(self):
        """Test operations with negative numbers."""
        assert self.calc.add(-5, -3) == -8
        assert self.calc.subtract(-5, -3) == -2
        assert self.calc.multiply(-2, -3) == 6
        assert self.calc.divide(-6, -2) == 3

    def test_zero_operations(self):
        """Test operations involving zero."""
        assert self.calc.add(0, 0) == 0
        assert self.calc.subtract(0, 0) == 0
        assert self.calc.multiply(0, 5) == 0
        assert self.calc.divide(0, 5) == 0
        assert self.calc.power(0, 5) == 0
        assert self.calc.power(5, 0) == 1


if __name__ == "__main__":
    pytest.main([__file__])
