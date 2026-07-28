def print_fibonacci_terms(n):
    """Prints the first n terms of the Fibonacci sequence using a loop."""
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    print("Fibonacci sequence:", " ".join(str(num) for num in sequence))


def is_fibonacci_number(num):
    """Returns True if num appears in the Fibonacci sequence, using a loop."""
    if num < 0:
        return False

    a, b = 0, 1
    while a <= num:
        if a == num:
            return True
        a, b = b, a + b

    return False


def main():
    n_input = input("How many terms? ")
    try:
        n = int(n_input)
    except ValueError:
        print("Error: Please enter a valid integer.")
        return

    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    print_fibonacci_terms(n)

    num_input = input("Enter a number to check: ")
    try:
        num = int(num_input)
    except ValueError:
        print("Error: Please enter a valid integer.")
        return

    if is_fibonacci_number(num):
        print(f"{num} is a Fibonacci number.")
    else:
        print(f"{num} is NOT a Fibonacci number.")


if __name__ == "__main__":
    main()
