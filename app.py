# filename: app.py

FILENAME = "tasks.txt"

# Load tasks from file
tasks = []
try:
    with open(FILENAME, "r") as file:
        tasks = [line.strip() for line in file.readlines()]
except FileNotFoundError:
    # If file doesn't exist, start with empty list
    tasks = []

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Delete Task\n4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        # Save immediately
        with open(FILENAME, "w") as file:
            for t in tasks:
                file.write(t + "\n")
        print("Task added!")

    elif choice == "2":
        if not tasks:
            print("No tasks yet!")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks):
                print(f"{i+1}. {t}")

    elif choice == "3":
        if not tasks:
            print("No tasks to delete!")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks):
                print(f"{i+1}. {t}")
            try:
                index = int(input("Enter task number to delete: "))
                if 1 <= index <= len(tasks):
                    removed = tasks.pop(index - 1)
                    # Save changes
                    with open(FILENAME, "w") as file:
                        for t in tasks:
                            file.write(t + "\n")
                    print(f"Deleted: {removed}")
                else:
                    print("Invalid number!")
            except ValueError:
                print("Please enter a valid number!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again.")
