def calculate_net_salary(basic_salary):
    """Calculate a simple illustrative salary: 10% allowance and 5% deduction."""
    if basic_salary <= 0:
        raise ValueError("Basic salary must be greater than zero.")

    allowance = basic_salary * 0.10
    deduction = basic_salary * 0.05
    net_salary = basic_salary + allowance - deduction

    return {
        "basic": basic_salary,
        "allowance": allowance,
        "deduction": deduction,
        "net_salary": net_salary,
    }
