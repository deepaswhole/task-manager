print("Welcome to the Task Manager!")
tasks = []

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. Task: {task['name']}, Priority: {task['priority']}, Due Date: {task['due_date']}, Completed: {task['completed']}")



