import json
print("Welcome to the Task Manager!")
tasks = []


def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. Task: {task['name']}, Priority: {task['priority']}, Due Date: {task['due_date']}, Completed: {task['completed']}")


def add_task(name, priority, due_date):
    tasks.append({"name": name, "priority": priority, "due_date": due_date, "completed": False})
    print(f"Task '{name}' added successfully!")


def mark_complete(task_number):
    try:
        tasks[task_number - 1]["completed"] = True
        print(f"Task {task_number} marked as complete!")
    except IndexError:
        print("Invalid task number!")


def delete_task(task_number):
    try:
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task['name']}' deleted successfully!")
    except IndexError:
        print("Invalid task number!")


def search_tasks_by_priority(priority):
    found_tasks = [task for task in tasks if task["priority"].lower() == priority.lower()]
    if found_tasks:
        for task in found_tasks:
            print(f"Task: {task['name']}, Priority: {task['priority']}, Due Date: {task['due_date']}, Completed: {task['completed']}")
    else:
        print(f"No tasks found with priority '{priority}'.")


def search_tasks_by_due_date(due_date):
    found_tasks = [task for task in tasks if task["due_date"] == due_date]
    if found_tasks:
        for task in found_tasks:
            print(f"Task: {task['name']}, Priority: {task['priority']}, Due Date: {task['due_date']}, Completed: {task['completed']}")
    else:
        print(f"No tasks found with due date '{due_date}'.")


def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)
    print("Tasks saved to file!")


def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
        print("Tasks loaded from file!")
    except FileNotFoundError:
        print("No saved tasks found.")


def task_summary():
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task["completed"])
    pending_tasks = total_tasks - completed_tasks
    print("Update summary 2")
    print(f"Total Tasks: {total_tasks}, Completed: {completed_tasks}, Pending: {pending_tasks}")


while True:
    print("\nOptions:")
    print("[1] View Tasks [2] Add Task [3] Mark Complete [4] Delete Task")
    print("[5] Search by Priority [6] Search by Due Date [7] Save Tasks [8] Load Tasks [9] Summary [10] Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        name = input("Enter task name: ")
        priority = input("Enter task priority: ")
        due_date = input("Enter due date (YYYY-MM-DD): ")
        add_task(name, priority, due_date)
    elif choice == "3":
        try:
            task_number = int(input("Enter task number to mark complete: "))
            mark_complete(task_number)
        except ValueError:
            print("Please enter a valid number!")
    elif choice == "4":
        try:
            task_number = int(input("Enter task number to delete: "))
            delete_task(task_number)
        except ValueError:
            print("Please enter a valid number!")
    elif choice == "5":
        priority = input("Enter priority to search: ")
        search_tasks_by_priority(priority)
    elif choice == "6":
        due_date = input("Enter due date to search (YYYY-MM-DD): ")
        search_tasks_by_due_date(due_date)
    elif choice == "7":
        save_tasks()
    elif choice == "8":
        load_tasks()
    elif choice == "9":
        task_summary()
    elif choice == "10":
        print("Goodbye!")
        break
    else:
        print("Invalid option!")
