# DevSecOps CI/CD Demo Repository

This is a basic repository to demonstrate CI/CD (Continuous Integration/Continuous Deployment) using GitHub Actions.

## Project Structure

```
devsecops/
├── .github/
│   └── workflows/
│       ├── ci.yml          # Continuous Integration workflow
│       └── cd.yml          # Continuous Deployment workflow
├── src/
│   ├── __init__.py
│   ├── calculator.py       # Simple calculator module
│   └── main.py            # Main application entry point
├── tests/
│   ├── __init__.py
│   ├── test_calculator.py  # Unit tests for calculator
│   └── test_main.py       # Integration tests
├── requirements.txt        # Python dependencies
├── requirements-dev.txt    # Development dependencies
├── .gitignore             # Git ignore file
└── README.md              # This file
```

## Features

- **Simple Calculator Application**: Basic arithmetic operations
- **Unit Tests**: Comprehensive test coverage using pytest
- **GitHub Actions CI**: Automated testing on push/PR
- **GitHub Actions CD**: Automated deployment (simulated)
- **Code Quality**: Linting and formatting checks

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd devsecops
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### Running the Application

```bash
python src/main.py
```

### Running Tests

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=src

# Run tests with verbose output
pytest -v
```

### Code Quality Checks

```bash
# Linting
flake8 src/ tests/

# Formatting
black src/ tests/

# Type checking
mypy src/
```

## CI/CD Pipeline

### Continuous Integration (CI)

The CI pipeline runs on every push and pull request:

1. **Code Quality Checks**:
   - Linting with flake8
   - Code formatting with black
   - Type checking with mypy

2. **Testing**:
   - Unit tests with pytest
   - Coverage reporting
   - Test results summary

3. **Security**:
   - Dependency vulnerability scanning
   - Code security analysis

### Continuous Deployment (CD)

The CD pipeline runs on successful CI completion:

1. **Build**: Create deployment artifacts
2. **Test**: Run integration tests
3. **Deploy**: Simulate deployment to staging/production

## GitHub Actions Workflows

### CI Workflow (`.github/workflows/ci.yml`)

- Triggers: `push`, `pull_request`
- Jobs:
  - Code Quality
  - Testing
  - Security Scanning

### CD Workflow (`.github/workflows/cd.yml`)

- Triggers: `workflow_run` (after successful CI)
- Jobs:
  - Build
  - Deploy to Staging
  - Deploy to Production (manual approval)

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-feature`
3. Make your changes
4. Run tests: `pytest`
5. Commit your changes: `git commit -am 'Add new feature'`
6. Push to the branch: `git push origin feature/new-feature`
7. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 