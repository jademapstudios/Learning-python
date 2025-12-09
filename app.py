"""print("Welcome to MiList")

def main():
    task = []

    while True:
        print("***** To do List *****")
        print("1. Add a Task")
        print("2. Show Task List")
        print("3. Mark a Task as Done")
        print("4. Exit")

        Choice = input("enter Your Choice:  ")

        if Choice == '1':
            print()
            n_task = int(input("How many Task do you wish to add?:  "))

            for i in range (n_task):
                tasks = input("Enter the Task:  ")
                task.append({"tasks1"
                "": task, "done": False})
                print("Task added!")

        elif Choice == '2':
            print("\nTasks:")
            for index, task in enumerate(task):
                status = "done" if task["done"] else "Not Done"
                print(f"{index + 1}. {task['task']} - {status}")

        elif Choice == '3':
            task_index = int(input("Enter the task Number To mark as Done:  ")) - 1
            if 0 <= task_index < len(task):
                task[task_index]["done"] = True
                print("Task Marked as Done!")
            else:
                print("invalid Task number.")

        elif Choice == '4':
            print("Exiting MiList...")
            break

        else:
            print("invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    """