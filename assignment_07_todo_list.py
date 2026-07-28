def add_task(tasks):
    """Prompts for a task description and adds it to the list."""
    description = input("Enter task: ")
    tasks.append(description)
    print(f'Task added: "{description}"')


def view_tasks(tasks):
    """Displays all tasks, numbered from 1. Shows a message if empty."""
    if not tasks:
        print("Your to-do list is empty.")
        return

    print("Your Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def delete_task(tasks):
    """Shows the task list, then removes the task the user picks by number."""
    if not tasks:
        print("Your to-do list is empty. Nothing to delete.")
        return

    view_tasks(tasks)
    choice = input("Enter task number to delete: ")

    try:
        index = int(choice)
    except ValueError:
        print("Error: Please enter a valid task number.")
        return

    if index < 1 or index > len(tasks):
        print("Error: Invalid task number.")
        return

    removed = tasks.pop(index - 1)
    print(f'Task "{removed}" has been removed.')


def print_menu():
    print("\n============================")
    print("     TO-DO LIST MENU")
    print("============================")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")


def main():
    tasks = []

    while True:
        print_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: Please choose a valid option (1-4).")


if __name__ == "__main__":
    main()
