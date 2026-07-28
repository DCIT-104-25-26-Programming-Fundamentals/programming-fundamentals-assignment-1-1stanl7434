def read_matrix(rows, cols, label=""):
    """Reads a matrix of the given size from the user, one row per line."""
    matrix = []
    for i in range(rows):
        while True:
            row_input = input(f"Enter row {i + 1}{(' of ' + label) if label else ''}: ")
            values = row_input.split()
            if len(values) != cols:
                print(f"Error: Expected {cols} values, got {len(values)}. Try again.")
                continue
            try:
                row = [float(v) for v in values]
            except ValueError:
                print("Error: Please enter valid numbers separated by spaces.")
                continue
            matrix.append(row)
            break
    return matrix


def print_matrix(matrix, title=""):
    """Displays a matrix in a neat, aligned grid format."""
    if title:
        print(f"\n{title}")
    for row in matrix:
        formatted_row = []
        for value in row:
            if value == int(value):
                formatted_row.append(f"{int(value):>6}")
            else:
                formatted_row.append(f"{value:>6.2f}")
        print(" ".join(formatted_row))


def transpose_matrix(matrix):
    """Returns the transpose of the given matrix using nested loops."""
    rows = len(matrix)
    cols = len(matrix[0])
    result = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result


def add_matrices(a, b):
    """Returns the element-wise sum of two same-sized matrices."""
    rows = len(a)
    cols = len(a[0])
    result = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = a[i][j] + b[i][j]

    return result


def multiply_matrices(a, b):
    """Returns the matrix product of A (M x N) and B (N x P)."""
    m = len(a)
    n = len(a[0])
    p = len(b[0])
    result = [[0] * p for _ in range(m)]

    for i in range(m):
        for j in range(p):
            total = 0
            for k in range(n):
                total += a[i][k] * b[k][j]
            result[i][j] = total

    return result


def get_dimensions(row_label="rows", col_label="columns"):
    """Prompts for and returns valid positive integer dimensions."""
    while True:
        try:
            rows = int(input(f"Enter number of {row_label}: "))
            cols = int(input(f"Enter number of {col_label}: "))
            if rows <= 0 or cols <= 0:
                print("Error: Dimensions must be positive integers.")
                continue
            return rows, cols
        except ValueError:
            print("Error: Please enter valid integers.")


def do_transpose():
    rows, cols = get_dimensions()
    matrix = read_matrix(rows, cols)
    print_matrix(matrix, "Original Matrix:")
    result = transpose_matrix(matrix)
    print_matrix(result, "Transposed Matrix:")


def do_addition():
    rows, cols = get_dimensions()
    print("Matrix A:")
    a = read_matrix(rows, cols, "A")
    print("Matrix B:")
    b = read_matrix(rows, cols, "B")
    print_matrix(a, "Matrix A:")
    print_matrix(b, "Matrix B:")
    result = add_matrices(a, b)
    print_matrix(result, "Sum (A + B):")


def do_multiplication():
    m, n = get_dimensions("rows in A", "columns in A")
    print("Matrix A:")
    a = read_matrix(m, n, "A")

    while True:
        n_b = int(input("Enter number of rows in B: "))
        if n_b != n:
            print(f"Error: Rows in B must equal columns in A ({n}). Try again.")
            continue
        break
    p = int(input("Enter number of columns in B: "))

    print("Matrix B:")
    b = read_matrix(n_b, p, "B")

    print_matrix(a, "Matrix A:")
    print_matrix(b, "Matrix B:")
    result = multiply_matrices(a, b)
    print_matrix(result, "Product (A x B):")


def main():
    while True:
        print("\nMatrix Operations")
        print("1. Transpose a Matrix")
        print("2. Add Two Matrices")
        print("3. Multiply Two Matrices")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            do_transpose()
        elif choice == "2":
            do_addition()
        elif choice == "3":
            do_multiplication()
        elif choice == "4":
            break
        else:
            print("Error: Please choose a valid option (1-4).")


if __name__ == "__main__":
    main()
