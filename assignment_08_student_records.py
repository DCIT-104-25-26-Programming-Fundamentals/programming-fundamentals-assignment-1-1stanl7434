def add_student(students):
    """Prompts for a student's name, ID, and scores, then saves the record."""
    name = input("Student name: ")

    id_input = input("Student ID: ")
    try:
        student_id = int(id_input)
    except ValueError:
        print("Error: Student ID must be a number.")
        return

    count_input = input("How many scores? ")
    try:
        count = int(count_input)
    except ValueError:
        print("Error: Please enter a valid integer.")
        return

    if count <= 0:
        print("Error: Number of scores must be a positive integer.")
        return

    scores = []
    for i in range(1, count + 1):
        score_input = input(f"Enter score {i}: ")
        try:
            score = float(score_input)
        except ValueError:
            print("Error: Please enter a valid number.")
            return
        if score.is_integer():
            score = int(score)
        scores.append(score)

    student = {
        "name": name,
        "id": student_id,
        "scores": scores
    }
    students.append(student)
    print(f'Student "{name}" added successfully.')


def calculate_average(scores):
    """Returns the average of a list of scores, rounded to 2 decimal places."""
    return round(sum(scores) / len(scores), 2)


def display_all_students(students):
    """Prints a formatted table of all students with their scores and average."""
    if not students:
        print("No students have been added yet.")
        return

    print("-" * 50)
    print(f"{'Name':<15}{'ID':<12}{'Scores':<15}{'Average':<10}")
    print("-" * 50)
    for student in students:
        scores_str = ", ".join(str(s) for s in student["scores"])
        average = calculate_average(student["scores"])
        print(f"{student['name']:<15}{student['id']:<12}{scores_str:<15}{average:<10}")
    print("-" * 50)


def find_student_average(students):
    """Looks up a student by ID and displays their average score."""
    id_input = input("Enter student ID: ")
    try:
        student_id = int(id_input)
    except ValueError:
        print("Error: Please enter a valid student ID.")
        return

    for student in students:
        if student["id"] == student_id:
            average = calculate_average(student["scores"])
            print(f"{student['name']}'s average score: {average}")
            return

    print(f"Error: No student found with ID {student_id}.")


def print_menu():
    print("\n================================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")


def main():
    students = []

    while True:
        print_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_all_students(students)
        elif choice == "3":
            find_student_average(students)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: Please choose a valid option (1-4).")


if __name__ == "__main__":
    main()
