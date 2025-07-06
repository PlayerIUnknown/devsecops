#!/usr/bin/env python3
"""
Main application entry point for the DevSecOps CI/CD demo.
Demonstrates the calculator functionality.
"""

import sys
from calculator import Calculator


def main() -> int:
    """Main application function."""
    print("🚀 DevSecOps CI/CD Demo Calculator")
    print("=" * 40)
    
    # Create calculator instance
    calc = Calculator()
    
    # Demonstrate basic operations
    print("\n📊 Basic Operations Demo:")
    print(f"Addition: 5 + 3 = {calc.add(5, 3)}")
    print(f"Subtraction: 10 - 4 = {calc.subtract(10, 4)}")
    print(f"Multiplication: 6 * 7 = {calc.multiply(6, 7)}")
    print(f"Division: 15 / 3 = {calc.divide(15, 3)}")
    print(f"Power: 2 ^ 8 = {calc.power(2, 8)}")
    
    # Demonstrate error handling
    print(f"\n⚠️  Error Handling Demo:")
    print(f"Division by zero: 10 / 0 = {calc.divide(10, 0)}")
    
    # Show calculation history
    print(f"\n📝 Calculation History:")
    for i, calculation in enumerate(calc.get_history(), 1):
        print(f"  {i}. {calculation}")
    
    print(f"\n✅ Demo completed successfully!")
    return 0


if __name__ == "__main__":
    sys.exit(main()) 