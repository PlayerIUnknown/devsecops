"""
Simple calculator module for CI/CD demonstration.
Provides basic arithmetic operations.
"""

from typing import Union, Optional


class Calculator:
    """A simple calculator class for basic arithmetic operations."""

    def __init__(self) -> None:
        self.history = []

    def add(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Add two numbers."""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Subtract b from a."""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Multiply two numbers."""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(
        self, a: Union[int, float], b: Union[int, float]
    ) -> Optional[Union[int, float]]:
        """Divide a by b. Returns None if b is zero."""
        if b == 0:
            self.history.append(f"{a} / {b} = Error: Division by zero")
            return None
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result

    def power(
        self, base: Union[int, float], exponent: Union[int, float]
    ) -> Union[int, float]:
        """Raise base to the power of exponent."""
        result = base**exponent
        self.history.append(f"{base} ^ {exponent} = {result}")
        return result

    def get_history(self) -> list[str]:
        """Get calculation history."""
        return self.history.copy()

    def clear_history(self) -> None:
        """Clear calculation history."""
        self.history.clear()


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Add two numbers (function version)."""
    return a + b


def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Subtract b from a (function version)."""
    return a - b


def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Multiply two numbers (function version)."""
    return a * b


def divide(a: Union[int, float], b: Union[int, float]) -> Optional[Union[int, float]]:
    """Divide a by b (function version). Returns None if b is zero."""
    if b == 0:
        return None
    return a / b
