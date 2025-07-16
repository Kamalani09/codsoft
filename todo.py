import json
import os
# Load existing tasks if any
def load_tasks(filename='tasks.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return []
# Save tasks to file
def save_tasks(tasks, filename='tasks.json'):
    with open(filename, 'w') as f:
        json.dump(tasks, f, indent=4)
# Display tasks
def show_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, 1):
            status = "✅" if task['done'] else "❌"
            print(f"{i}. {task['title']} [{status}]")
# Main app loop
def main():
    tasks = load_tasks()
    while True:
        print("\n--- TO-DO LIST ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            title = input("Enter task title: ")
            tasks.append({"title": title, "done": False})
            save_tasks(tasks)
        elif choice == '2':
            show_tasks(tasks)
        elif choice == '3':
            show_tasks(tasks)
            idx = int(input("Enter task number to mark done: ")) - 1
            if 0 <= idx < len(tasks):
                tasks[idx]['done'] = True
                save_tasks(tasks)
            else:
                print("Invalid task number.")
        elif choice == '4':
            show_tasks(tasks)
            idx = int(input("Enter task number to delete: ")) - 1
            if 0 <= idx < len(tasks):
                tasks.pop(idx)
                save_tasks(tasks)
            else:
                print("Invalid task number.")
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")
if __name__ == "__main__":
    main()

