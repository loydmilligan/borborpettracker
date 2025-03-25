# BorBorPetTracker Development Guidelines

## Commands
- Install: `pip install -e .`
- Format: `black .`
- Lint: `flake8 . && mypy .`
- Test all: `pytest`
- Test single: `pytest tests/path/to/test_file.py::TestClass::test_function`
- Run app: `python -m borbor_pet_tracker`

## Style Guidelines
- **Formatting**: Use Black with 88-character line length
- **Imports**: Group standard library, third-party, then local imports with a blank line between groups
- **Naming**: snake_case for functions/variables, PascalCase for classes, UPPER_CASE for constants
- **Types**: Use type hints for all function parameters and return values
- **Documentation**: Docstrings follow Google style (parameters, returns, raises)
- **Error handling**: Use specific exceptions, handle appropriately at boundaries
- **Testing**: Use pytest fixtures extensively, aim for >80% coverage

## Repository Structure
- `borbor_pet_tracker/` - Main package code
- `tests/` - Test files (mirror package structure)
- `docs/` - Documentation files