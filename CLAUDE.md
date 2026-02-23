# CLAUDE.md - Project Documentation

## Project Overview

This is a **multi-purpose Python project** combining:
1. **Hello World Application** - A simple utility with greeting and arithmetic functions
2. **Data Analysis Pipeline** - CS Students Performance dataset analysis using Jupyter notebooks
3. **Flask Web Application** - A news article web application with Flask

The project serves educational purposes for PhD coursework, demonstrating various Python development patterns and data science workflows.

## Technology Stack

### Core Technologies
- **Python 3.10+** - Primary programming language with type annotations
- **Flask** - Web framework for the news application (`app.py`)
- **Jupyter Notebook** - Interactive data analysis environment
- **Pandas, NumPy** - Data manipulation and numerical computing
- **Matplotlib, Seaborn** - Data visualization libraries
- **Kaggle CLI** - Dataset download utility

### Development Tools
- **unittest** - Python standard library testing framework
- **nbconvert** - Jupyter notebook execution and conversion
- **git** - Version control

## Project Structure

```
helloworld/
├── main.py                     # Core application with add() and main() functions
├── test_main.py               # Unit tests for main.py functions
├── app.py                     # Flask web application (news articles)
├── run_analysis.py            # Interactive data analysis pipeline
├── execute_notebook.py        # Batch notebook execution script
├── data_analysis.ipynb        # Jupyter notebook for CS students data analysis
├── cs_students.csv            # Dataset (auto-downloaded from Kaggle)
├── readme.md                  # Project introduction and usage guide
├── plan.md                    # Project planning and specifications
└── CLAUDE.md                  # This file
```

## Setup Instructions

### 1. Basic Setup (No Dependencies)
For the Hello World application only:

```bash
# Navigate to project directory
cd helloworld

# Run the application
python main.py

# Run tests
python -m unittest test_main.py -v
```

### 2. Data Analysis Setup
For the full data analysis pipeline:

```bash
# Install dependencies
pip install pandas numpy matplotlib seaborn scipy jupyter nbconvert kaggle

# Option A: Interactive mode (opens Jupyter notebook)
python run_analysis.py

# Option B: Batch execution (auto-runs and saves output)
python execute_notebook.py
```

### 3. Flask Web Application Setup
For the news article website:

```bash
# Install Flask
pip install flask

# Run the web server
python app.py

# Access the application
# Open browser and navigate to http://localhost:5000
```

## Core Components

### 1. Hello World Application (`main.py`)

**Functions:**
- `main() -> None` - Prints "I am the world" to stdout
- `add(a: int | float, b: int | float) -> int | float` - Adds two numbers and returns the sum

**Type System:**
- Preserves numeric types: returns `int` if both args are `int`, otherwise `float`
- Example: `add(2, 3)` returns `5`, `add(1.5, 2)` returns `3.5`

**Testing:**
Run comprehensive unit tests with:
```bash
python -m unittest test_main.py -v
```

### 2. Flask Web Application (`app.py`)

**Routes:**
- `GET /` - Home page displaying list of news articles
- `GET /article/<id>` - Individual article detail page

**Data:**
- Three sample articles (Python 3.13, AI Models, Tech Earnings)
- Each article includes: id, title, summary, content, date

**Template Requirements:**
- `templates/index.html` - Home page listing articles
- `templates/article.html` - Article detail page

### 3. Data Analysis Pipeline

**Input:** CS Students Performance dataset (Kaggle)
**Processing:** Jupyter notebook with pandas, numpy, visualization
**Output:** `data_analysis_output.ipynb` with executed cells and results

**Execution Methods:**
- `run_analysis.py` - Interactive (launches Jupyter server)
- `execute_notebook.py` - Batch mode (headless execution)

## Common Operations

### Run Tests
```bash
# Simple run
python -m unittest test_main.py

# Verbose output
python -m unittest test_main.py -v

# Specific test
python -m unittest test_main.py.TestAdd
```

### Run Flask Application
```bash
python app.py
# Then open http://localhost:5000 in browser
# Debug mode is enabled (auto-reload on code changes)
```

### Execute Data Analysis
```bash
# Option 1: Interactive
python run_analysis.py

# Option 2: Batch (outputs to CSV/HTML)
python execute_notebook.py

# Option 3: Direct Jupyter
jupyter notebook data_analysis.ipynb
```

### Download Dataset Manually (if Kaggle CLI fails)
1. Visit: https://www.kaggle.com/datasets/zahranusratt/cs-students-performance-dataset
2. Download `cs_students.csv`
3. Place in project root directory

### View Results
- Executed notebook: `data_analysis_output.ipynb`
- CSV dataset: `cs_students.csv`

## Best Practices

### Python Code Style
- Use type hints for all functions (PEP 484)
- Follow PEP 8 naming conventions
- Use `if __name__ == "__main__":` guard for executable modules
- Include docstrings for all functions and modules

### Testing
- Write unit tests for all public functions
- Use `unittest` framework (standard library)
- Test edge cases: zero, negatives, type preservation
- Run tests before committing changes

### Data Analysis
- Use Jupyter notebooks for exploratory analysis
- Comment complex analytical steps
- Version both notebook source and executed output
- Document data source and processing steps

### Version Control
```bash
# Before committing
git status
git diff

# Commit with clear messages
git add .
git commit -m "Brief description of changes"

# Track untracked files (data is in git status output)
git add cs_students.csv data_analysis.ipynb
```

## Dependencies Summary

### Minimal (Hello World only)
- Python 3.10+ (built-in libraries only)

### Standard (All features)
- `pandas` - Data manipulation
- `numpy` - Numerical computing
- `matplotlib` - Static plotting
- `seaborn` - Statistical visualization
- `scipy` - Scientific computing
- `jupyter` - Notebook interface
- `nbconvert` - Notebook execution
- `flask` - Web framework
- `kaggle` - Dataset download

### Development
- `unittest` - Built into Python

## Next Steps

1. **Add HTML Templates** (Required for Flask app)
   - Create `templates/` directory
   - Build `index.html` with article listing
   - Build `article.html` with detail view

2. **Expand Data Analysis**
   - Add more statistical analyses
   - Create advanced visualizations
   - Generate summary reports

3. **Enhance Testing**
   - Add integration tests for Flask routes
   - Test notebook execution in CI/CD

4. **Documentation**
   - Add API documentation (Flask routes)
   - Document analysis methodology
   - Create usage examples

5. **Deployment**
   - Containerize Flask app (Docker)
   - Set up automated testing (GitHub Actions)
   - Deploy web application (Heroku, AWS, etc.)

## Environment Notes

- **Windows PowerShell** - Use `python` instead of `python3`
- **Python Path** - Ensure Python 3.10+ is in system PATH
- **Jupyter Server** - Runs on `http://localhost:8888` by default
- **Flask Server** - Runs on `http://localhost:5000` with debug enabled

## Troubleshooting

### Module Import Errors
```bash
# Reinstall dependencies
pip install --upgrade pandas numpy matplotlib seaborn scipy jupyter flask

# Verify installation
python -c "import pandas; print(pandas.__version__)"
```

### Kaggle Dataset Download Fails
- Install Kaggle CLI: `pip install kaggle`
- Configure credentials: `kaggle auth --username YOUR_USERNAME --key YOUR_API_KEY`
- Or download manually from Kaggle website

### Flask Port Already in Use
```bash
# Change port in app.py
app.run(debug=True, port=5001)  # Use different port
```

### Jupyter Notebook Issues
```bash
# Clear kernel cache
jupyter kernelspec list
jupyter kernelspec remove python3

# Reinstall jupyter
pip uninstall jupyter -y
pip install jupyter
```

## Project Metadata

- **Type:** Educational/Multi-purpose Python Application
- **Language:** Python 3.10+
- **License:** (Specify as needed)
- **Created:** PhD Program - Code courses
- **Last Updated:** February 2026
