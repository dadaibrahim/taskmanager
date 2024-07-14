class Task:
    def __init__(self, task_id, title, description, status):
        self.id = task_id
        self.title = title
        self.description = description
        self.status = status

    def __str__(self):
        return f"[{self.id}] {self.title} - {self.description} (Status: {self.status})"

def create_task(task_list):
    task_id = len(task_list) + 1
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    status = input("Enter task status (To Do, In Progress, Done): ")
    task = Task(task_id, title, description, status)
    task_list.append(task)
    print("Task created successfully.")

def read_tasks(task_list):
    if not task_list:
        print("No tasks available.")
    else:
        for task in task_list:
            print(task)

def update_task(task_list):
    task_id = int(input("Enter task ID to update: "))
    for task in task_list:
        if task.id == task_id:
            task.title = input("Enter new task title: ")
            task.description = input("Enter new task description: ")
            task.status = input("Enter new task status (To Do, In Progress, Done): ")
            print("Task updated successfully.")
            return
    print("Task not found.")

def delete_task(task_list):
    task_id = int(input("Enter task ID to delete: "))
    for task in task_list:
        if task.id == task_id:
            task_list.remove(task)
            print("Task deleted successfully.")
            return
    print("Task not found.")

def main():
    task_list = []
    while True:
        print("\nTask Manager")
        print("1. Create Task")
        print("2. Read Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            create_task(task_list)
        elif choice == '2':
            read_tasks(task_list)
        elif choice == '3':
            update_task(task_list)
        elif choice == '4':
            delete_task(task_list)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
