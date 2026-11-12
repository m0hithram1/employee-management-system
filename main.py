from database import initialize_database
from employee_service import (
    add_employee, list_employees, find_employee, update_employee,
    delete_employee, get_payroll_summary
)
from payroll import calculate_net_salary
from utils import read_int, read_float, read_non_empty, pause


def show_menu():
    print("\n" + "=" * 48)
    print("        EMPLOYEE MANAGEMENT SYSTEM")
    print("=" * 48)
    print("1. Add employee")
    print("2. View all employees")
    print("3. Search employee")
    print("4. Update employee")
    print("5. Delete employee")
    print("6. Calculate employee salary")
    print("7. Payroll summary")
    print("0. Exit")
    print("=" * 48)


def add_employee_screen():
    print("\n--- Add Employee ---")
    name = read_non_empty("Full name: ")
    age = read_int("Age: ", minimum=18, maximum=100)
    department = read_non_empty("Department: ")
    designation = read_non_empty("Designation: ")
    salary = read_float("Monthly basic salary (₹): ", minimum=0.01)
    email = input("Email (optional): ").strip() or None

    employee_id = add_employee(name, age, department, designation, salary, email)
    print(f"\nEmployee added successfully. Employee ID: {employee_id}")


def view_employees_screen():
    print("\n--- Employee Records ---")
    employees = list_employees()
    if not employees:
        print("No employee records found.")
        return
    print(f"{'ID':<6} {'NAME':<22} {'DEPARTMENT':<16} {'DESIGNATION':<20} {'SALARY':>12}")
    print("-" * 82)
    for emp in employees:
        print(f"{emp['id']:<6} {emp['name'][:21]:<22} {emp['department'][:15]:<16} "
              f"{emp['designation'][:19]:<20} ₹{emp['basic_salary']:>10,.2f}")


def search_employee_screen():
    employee_id = read_int("Enter employee ID: ", minimum=1)
    emp = find_employee(employee_id)
    if not emp:
        print("Employee not found.")
        return
    print("\nEmployee details")
    for key, value in emp.items():
        print(f"{key.replace('_', ' ').title()}: {value}")


def update_employee_screen():
    employee_id = read_int("Enter employee ID to update: ", minimum=1)
    emp = find_employee(employee_id)
    if not emp:
        print("Employee not found.")
        return

    print("Press Enter to keep the current value.")
    name = input(f"Name [{emp['name']}]: ").strip() or emp["name"]
    department = input(f"Department [{emp['department']}]: ").strip() or emp["department"]
    designation = input(f"Designation [{emp['designation']}]: ").strip() or emp["designation"]
    salary_text = input(f"Basic salary [{emp['basic_salary']}]: ").strip()
    salary = float(salary_text) if salary_text else emp["basic_salary"]
    if salary <= 0:
        print("Salary must be greater than zero.")
        return

    update_employee(employee_id, name, department, designation, salary)
    print("Employee updated successfully.")


def delete_employee_screen():
    employee_id = read_int("Enter employee ID to delete: ", minimum=1)
    emp = find_employee(employee_id)
    if not emp:
        print("Employee not found.")
        return
    confirm = input(f"Delete {emp['name']} (ID {employee_id})? Type YES to confirm: ")
    if confirm == "YES":
        delete_employee(employee_id)
        print("Employee deleted.")
    else:
        print("Deletion cancelled.")


def salary_screen():
    employee_id = read_int("Enter employee ID: ", minimum=1)
    emp = find_employee(employee_id)
    if not emp:
        print("Employee not found.")
        return
    result = calculate_net_salary(emp["basic_salary"])
    print(f"\nSalary breakdown for {emp['name']}")
    print(f"Basic salary : ₹{result['basic']:,.2f}")
    print(f"Allowance    : ₹{result['allowance']:,.2f} (10% of basic)")
    print(f"Deduction    : ₹{result['deduction']:,.2f} (5% of basic)")
    print(f"Net salary   : ₹{result['net_salary']:,.2f}")


def payroll_summary_screen():
    summary = get_payroll_summary()
    print("\n--- Payroll Summary ---")
    print(f"Number of employees : {summary['employee_count']}")
    print(f"Total basic payroll : ₹{summary['total_basic']:,.2f}")
    print(f"Estimated net payroll: ₹{summary['total_net']:,.2f}")


def main():
    initialize_database()
    actions = {
        "1": add_employee_screen,
        "2": view_employees_screen,
        "3": search_employee_screen,
        "4": update_employee_screen,
        "5": delete_employee_screen,
        "6": salary_screen,
        "7": payroll_summary_screen,
    }
    print("Welcome! Your employee database is ready.")
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        if choice == "0":
            print("Thank you for using Employee Management System. Goodbye!")
            break
        action = actions.get(choice)
        if action:
            try:
                action()
            except ValueError as error:
                print(f"Input error: {error}")
            except Exception as error:
                print(f"Something went wrong: {error}")
            pause()
        else:
            print("Invalid choice. Please select a number from 0 to 7.")


if __name__ == "__main__":
    main()
