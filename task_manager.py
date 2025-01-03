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


