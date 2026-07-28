def calculate_sum(numbers):
    """Returns the sum of all numbers in the list (no built-in sum())."""
    total = 0
    for num in numbers:
        total += num
    return total


def calculate_average(numbers):
    """Returns the average of the numbers in the list."""
    total = calculate_sum(numbers)
    return total / len(numbers)


def find_maximum(numbers):
    """Returns the largest number in the list (no built-in max())."""
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest


def find_minimum(numbers):
    """Returns the smallest number in the list (no built-in min())."""
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest


def main():
    n_input = input("How many numbers? ")

    try:
        n = int(n_input)
    except ValueError:
        print("Error: Please enter a valid integer.")
        return

    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    numbers = []
    for i in range(1, n + 1):
        value_input = input(f"Enter number {i}: ")
        try:
            value = float(value_input)
        except ValueError:
            print("Error: Please enter a valid number.")
            return
        if value.is_integer():
            value = int(value)
        numbers.append(value)

    total = calculate_sum(numbers)
    average = calculate_average(numbers)
    maximum = find_maximum(numbers)
    minimum = find_minimum(numbers)

    print("\nResults:")
    print(f"Sum:     {total}")
    print(f"Average: {average}")
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")


if __name__ == "__main__":
    main()
