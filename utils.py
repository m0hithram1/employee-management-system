def read_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def read_int(prompt, minimum=None, maximum=None):
    while True:
        try:
            value = int(input(prompt))
            if minimum is not None and value < minimum:
                print(f"Enter a value of at least {minimum}.")
                continue
            if maximum is not None and value > maximum:
                print(f"Enter a value no greater than {maximum}.")
                continue
            return value
        except ValueError:
            print("Please enter a whole number.")


def read_float(prompt, minimum=None):
    while True:
        try:
            value = float(input(prompt))
            if minimum is not None and value < minimum:
                print(f"Enter a value greater than or equal to {minimum}.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")


def pause():
    input("\nPress Enter to return to the menu...")
