
todo = []

while True:
    print("\n--- My To-Do Application List ---")
    
    print("1. Show tasks")
    print("2. Add task")
    print("3. Update task")
    print("4. Delete task")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        if len(todo) == 0:
            print("No tasks added yet.")
        else:
            print("\nMy tasks:")
            for i in range(len(todo)):
                print(i + 1, ".", todo[i])

    elif choice == "2":
        task = input("Enter your task: ")
        todo.append(task)
        print("Task added successfully.")


    elif choice == "3":
        if len(todo) == 0:
            print("Nothing to update.")
        else:
            for i in range(len(todo)):
                print(i + 1, ".", todo[i])

            num = int(input("Enter task number to update: "))
            if num > 0 and num <= len(todo):
                new_task = input("Enter new task: ")
                todo[num - 1] = new_task
                print("Task updated Successfully.")
            else:
                print("Invalid task number.")

    elif choice == "4":
        if len(todo) == 0:
            print("Nothing to delete.")
        else:
            for i in range(len(todo)):
                print(i + 1, ".", todo[i])

            num = int(input("Enter task number to delete: "))
            if num > 0 and num <= len(todo):
                todo.pop(num - 1)
                print("Task deleted Successfully.")
            else:
                print("Invalid task number.")

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Please enter a valid option.")
