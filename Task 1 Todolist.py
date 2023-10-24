 tasks = []
def add_task(task_name, due_date):
    task = {'task_name': task_name, 'due_date': due_date, 'status': 'Incomplete'}
    tasks.append(task)

def list_tasks():
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['task_name']} (Due: {task['due_date']}, Status: {task['status']})")
while True:
    print("To-Do List Application")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task_name = input("Enter task name: ")
        due_date = input("Enter due date (YYYY-MM-DD): ")
        add_task(task_name, due_date)
    elif choice == '2':
        list_tasks()
    # Add code to handle other choices here
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")
