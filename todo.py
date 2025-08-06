# todo.py - Console-based To-Do List Application

def load_tasks():
    """Load tasks from the file."""
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Save tasks to the file."""
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(tasks):
    """Add a new task to the list."""
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added!")

def view_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def remove_task(tasks):
    """Remove a task by number."""
    view_tasks(tasks)
    try:
        task_no = int(input("Enter task number to remove: "))
        if 0 < task_no <= len(tasks):
            tasks.pop(task_no - 1)
            print("Task removed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main program loop."""
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
