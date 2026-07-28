def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    """Returns a / b rounded to 2 decimal places. Raises ZeroDivisionError if b is 0."""
    if b == 0:
        raise ZeroDivisionError
    return round(a / b, 2)


def modulus(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a % b


def exponentiate(a, b):
    return a ** b


def get_numbers():
    """Prompts for two numbers and returns them as floats, or None on invalid input."""
    first_input = input("Enter first number : ")
    second_input = input("Enter second number: ")
    try:
        first = float(first_input)
        second = float(second_input)
    except ValueError:
        print("Error: Please enter valid numbers.")
        return None
    return first, second


def format_number(num):
    """Displays whole numbers without a trailing .0."""
    if num == int(num):
        return str(int(num))
    return str(num)


def print_menu():
    print("\n============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def main():
    symbols = {"1": "+", "2": "-", "3": "*", "4": "/", "5": "%", "6": "**"}

    while True:
        print_menu()
        choice = input("Select an operation (1-7): ")

        if choice == "7":
            print("Goodbye!")
            break

        if choice not in symbols:
            print("Error: Please choose a valid option (1-7).")
            continue

        numbers = get_numbers()
        if numbers is None:
            continue
        a, b = numbers

        try:
            if choice == "1":
                result = add(a, b)
            elif choice == "2":
                result = subtract(a, b)
            elif choice == "3":
                result = multiply(a, b)
            elif choice == "4":
                result = divide(a, b)
            elif choice == "5":
                result = modulus(a, b)
            elif choice == "6":
                result = exponentiate(a, b)
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
            continue

        symbol = symbols[choice]
        print(f"Result: {format_number(a)} {symbol} {format_number(b)} = {format_number(result)}")


if __name__ == "__main__":
    main()
