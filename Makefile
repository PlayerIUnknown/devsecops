 .PHONY: help install install-dev test test-cov lint format type-check security clean build run

# Default target
help:
	@echo "Available commands:"
	@echo "  install      - Install production dependencies"
	@echo "  install-dev  - Install development dependencies"
	@echo "  test         - Run tests"
	@echo "  test-cov     - Run tests with coverage"
	@echo "  lint         - Run linting checks"
	@echo "  format       - Format code with black"
	@echo "  type-check   - Run type checking with mypy"
	@echo "  security     - Run security checks"
	@echo "  clean        - Clean up build artifacts"
	@echo "  build        - Build the package"
	@echo "  run          - Run the application"

# Install production dependencies
install:
	pip install -r requirements.txt

# Install development dependencies
install-dev:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

# Run tests
test:
	pytest tests/ -v

# Run tests with coverage
test-cov:
	pytest tests/ -v --cov=src --cov-report=html --cov-report=term-missing

# Run linting
lint:
	flake8 src/ tests/ --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 src/ tests/ --count --exit-zero --max-complexity=10 --max-line-length=88 --statistics

# Format code
format:
	black src/ tests/

# Run type checking
type-check:
	mypy src/ --ignore-missing-imports --disallow-untyped-defs

# Run security checks
security:
	bandit -r src/ -f json -o bandit-report.json || true
	bandit -r src/ -f txt -o bandit-report.txt || true
	safety check --json --output safety-report.json || true
	safety check --text --output safety-report.txt || true

# Clean build artifacts
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf htmlcov/
	rm -rf .coverage
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete

# Build the package
build:
	python -m build

# Run the application
run:
	python src/main.py

# Setup pre-commit hooks
setup-hooks:
	pre-commit install

# Run all checks (for CI)
ci-check: lint type-check security test

# Development setup
dev-setup: install-dev setup-hooks
	@echo "Development environment setup complete!"
	@echo "Run 'make test' to verify everything is working."