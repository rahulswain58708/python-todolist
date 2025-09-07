'''Todo list-features:
1. Task add
2. View task
3. Task update
4. Task delete
'''
tasks = []

def add_task(task):
    tasks.append(task)
    return f"Task '{task}' added successfully!"

def view_task():
    if not tasks:
        return "No task found."
    result = "Your tasks:\n"
    for i, t in enumerate(tasks, start=1):
        result += f"{i}. {t}\n"
    return result

def update_task(index, new_task):
    if 1 <= index <= len(tasks):
        tasks[index-1] = new_task
        return f"Task {index} updated to '{new_task}'"
    else:
        return "Invalid task number."

def delete_task(index):
    if 1 <= index <= len(tasks):
        removed = tasks.pop(index-1)
        return f"Task '{removed}' deleted."
    else:
        return "Invalid task number."

while True:
    print("\n------ Todolist Menu -------")
    print("1. Add task")
    print("2. View task")
    print("3. Update task")
    print("4. Delete task")
    print("5. Exit")

    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("⚠️ Please enter a valid number.")
        continue

    if choice == 1:
        task = input("Enter task: ")
        print(add_task(task))

    elif choice == 2:
        print(view_task())

    elif choice == 3:
        print(view_task())
        index = int(input("Enter update task number: "))
        new_task = input("Enter new task: ")
        print(update_task(index, new_task))

    elif choice == 4:
        print(view_task())
        index = int(input("Enter delete task number: "))
        print(delete_task(index))

    elif choice == 5:
        print("Exit Menu ✅")
        break

    else:
        print("Invalid choice")
