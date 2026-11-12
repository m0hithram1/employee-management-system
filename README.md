# Employee Management System

A beginner-friendly command-line employee management application built with Python and SQLite. It demonstrates CRUD operations, input validation, modular Python code, and basic payroll calculations.

## Features

- Add, view, search, update, and delete employee records
- Store records persistently in a local SQLite database
- Validate required fields, age, and salary
- Calculate illustrative monthly net salary
- Display a payroll summary
- Run a small automated test suite

## Technology

- Python 3.10+
- SQLite (included with Python)
- Python standard library only; no third-party packages required

## Project structure

```text
Employee-Management-System/
├── main.py
├── database.py
├── employee_service.py
├── payroll.py
├── utils.py
├── employees.db          # created automatically on first run
├── tests/
│   └── test_payroll.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Run the application

1. Install Python 3.10 or newer.
2. Open this folder in VS Code.
3. Open the integrated terminal in this folder.
4. Run:

   ```bash
   python main.py
   ```

   On some Windows installations, use:

   ```powershell
   py main.py
   ```

The database file is created automatically the first time the application runs.

## Run tests

```bash
python -m unittest discover -s tests -v
```

On Windows, `py -m unittest discover -s tests -v` also works.

## Payroll note

The payroll calculation in this learning project uses a simple example: 10% allowance and 5% deduction. These are illustrative values, not legal, tax, or company payroll rules. Real payroll must follow the employer's policies and applicable laws.

## Future improvements

- Add role-based login for HR and administrators
- Export employee reports to CSV
- Add department and date filters
- Build a web interface using Flask
- Add audit logs and stronger validation

## GitHub

Create a new empty GitHub repository named `employee-management-system`, then push this project folder. Do not upload a real employee database or private employee information.
