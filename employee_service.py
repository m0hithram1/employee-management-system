from database import get_connection
from payroll import calculate_net_salary


def add_employee(name, age, department, designation, basic_salary, email=None):
    if not name.strip() or not department.strip() or not designation.strip():
        raise ValueError("Name, department, and designation are required.")
    if age < 18:
        raise ValueError("Employee age must be at least 18.")
    if basic_salary <= 0:
        raise ValueError("Salary must be greater than zero.")

    with get_connection() as connection:
        cursor = connection.execute(
            """INSERT INTO employees
               (name, age, department, designation, basic_salary, email)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (name.strip(), age, department.strip(), designation.strip(),
             basic_salary, email)
        )
        return cursor.lastrowid


def list_employees():
    with get_connection() as connection:
        rows = connection.execute(
            "SELECT * FROM employees ORDER BY id"
        ).fetchall()
        return [dict(row) for row in rows]


def find_employee(employee_id):
    with get_connection() as connection:
        row = connection.execute(
            "SELECT * FROM employees WHERE id = ?", (employee_id,)
        ).fetchone()
        return dict(row) if row else None


def update_employee(employee_id, name, department, designation, basic_salary):
    if basic_salary <= 0:
        raise ValueError("Salary must be greater than zero.")
    with get_connection() as connection:
        cursor = connection.execute(
            """UPDATE employees
               SET name = ?, department = ?, designation = ?, basic_salary = ?
               WHERE id = ?""",
            (name.strip(), department.strip(), designation.strip(),
             basic_salary, employee_id)
        )
        return cursor.rowcount > 0


def delete_employee(employee_id):
    with get_connection() as connection:
        cursor = connection.execute(
            "DELETE FROM employees WHERE id = ?", (employee_id,)
        )
        return cursor.rowcount > 0


def get_payroll_summary():
    employees = list_employees()
    total_basic = sum(emp["basic_salary"] for emp in employees)
    total_net = sum(
        calculate_net_salary(emp["basic_salary"])["net_salary"]
        for emp in employees
    )
    return {
        "employee_count": len(employees),
        "total_basic": total_basic,
        "total_net": total_net,
    }
