"""
Integration tests for the main application.
"""

import pytest
import sys
import os
from io import StringIO
from unittest.mock import patch

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import main


class TestMainApplication:
    """Integration tests for the main application."""
    
    def test_main_success(self):
        """Test that main function runs successfully and returns 0."""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            result = main()
            
            # Check return value
            assert result == 0
            
            # Check output contains expected content
            output = fake_output.getvalue()
            assert "DevSecOps CI/CD Demo Calculator" in output
            assert "Basic Operations Demo:" in output
            assert "Error Handling Demo:" in output
            assert "Calculation History:" in output
            assert "Demo completed successfully!" in output
    
    def test_main_demonstrates_all_operations(self):
        """Test that main demonstrates all calculator operations."""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            main()
            output = fake_output.getvalue()
            
            # Check that all operations are demonstrated
            assert "Addition: 5 + 3 = 8" in output
            assert "Subtraction: 10 - 4 = 6" in output
            assert "Multiplication: 6 * 7 = 42" in output
            assert "Division: 15 / 3 = 5.0" in output
            assert "Power: 2 ^ 8 = 256" in output
    
    def test_main_demonstrates_error_handling(self):
        """Test that main demonstrates error handling."""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            main()
            output = fake_output.getvalue()
            
            # Check that division by zero is handled
            assert "Division by zero: 10 / 0 = None" in output
    
    def test_main_shows_calculation_history(self):
        """Test that main shows calculation history."""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            main()
            output = fake_output.getvalue()
            
            # Check that history is displayed
            assert "Calculation History:" in output
            # Should have 6 calculations (5 successful + 1 error)
            assert "1. 5 + 3 = 8" in output
            assert "2. 10 - 4 = 6" in output
            assert "3. 6 * 7 = 42" in output
            assert "4. 15 / 3 = 5.0" in output
            assert "5. 2 ^ 8 = 256" in output
            assert "6. 10 / 0 = Error: Division by zero" in output


class TestMainAsScript:
    """Test main.py when run as a script."""
    
    def test_main_as_script(self):
        """Test that main.py can be run as a script."""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            # Import and run main as if it were executed as a script
            from main import main
            result = main()
            
            assert result == 0
            output = fake_output.getvalue()
            assert "DevSecOps CI/CD Demo Calculator" in output


class TestMainErrorHandling:
    """Test error handling in main application."""
    
    def test_main_imports_correctly(self):
        """Test that all imports work correctly."""
        try:
            from main import main
            assert callable(main)
        except ImportError as e:
            pytest.fail(f"Failed to import main: {e}")
    
    def test_main_returns_integer(self):
        """Test that main returns an integer exit code."""
        result = main()
        assert isinstance(result, int)
        assert result == 0


if __name__ == "__main__":
    pytest.main([__file__]) 