#Impoprting Major libaries
import json
#creating an external file
TASK_FILE = 'Milist.json'


#defining the loading function to load previously saved tasks list
def load_tasks():
    global list_of_tasks # Declares that we want to modify the global 'tasks' list
    
    try:
        # Open the file in read mode ('r')
        with open(TASK_FILE, 'r') as file:
            # Load the JSON data from the file back into the tasks list
            list_of_tasks = json.load(file)
        print(f"Loaded {len(list_of_tasks)} tasks from {TASK_FILE}.")
        
    except FileNotFoundError:
        # If the file doesn't exist yet (first time running), this is fine.
        print("Starting with an empty To-Do list.")
        tasks = [] # Ensure tasks is empty list if file doesn't exist
    
    except json.JSONDecodeError:
        # Handles cases where the file exists but is empty or corrupted
        print("Error reading task data. Starting fresh.")
        list_of_tasks = []
    return


#defining the saving function to save current tasks list
def save_tasks():
    # Open the file in write mode ('w'). This will create the file if it doesn't exist
    # or overwrite it if it does.
    with open(TASK_FILE, 'w') as file:
        # Dump (write) the Python list 'tasks' to the file in JSON format
        json.dump(list_of_tasks, file, indent=4) 
    print(f"Tasks successfully saved to {TASK_FILE}.")



#Defining a global variable for the list of tasks
list_of_tasks = []




#creating a function for each option available to the user
#for Option 1
def option_1(task_name):
    new_id = len(list_of_tasks) + 1
    new_task = {
        'name': task_name,
        'status': 'New',
        'id': new_id,
    }

    list_of_tasks.append(new_task)
    print(f"\nTask '{task_name}' added!")
    print(f"\nYour Task id is '{len(list_of_tasks)}'")


#For Option 2
def option2():
    print("\n--- Your To-Do List ---\n")
    if not list_of_tasks: # To Check if the list is empty
        print("\nNo tasks yet. \nTime to add some!")
        return

    # Used enumerate to get both the index (i) and the item (task)
    for i, task in enumerate(list_of_tasks):
        task_id = i + 1
        # We add 1 to i so the list starts at 1 for the user
        print(f"{task_id}. [{task['status']}] - {task['name']}")
    print("-----------------------")


#For Option 3
def option3(search_name, task_id):
    """
    Checks if a task with the given name exists in the global tasks list.
    Returns the task dictionary if found, otherwise returns None.
    """
    # 1. Iterate through every dictionary (task) in the 'tasks' list
    for new_task in list_of_tasks:
        # 2. Check if the value associated with the 'name' key 
        #    matches the task_name the user provided.
        if new_task['name'] == search_name and task_id == new_task['id']: 
            # 3. If a match is found, return the task dictionary immediately.
            new_task['status'] = 'pending'
            print(f"\nTask '{search_name}' is now Pending!")
            return
    # 4. If the loop finishes without finding a match, return None.
    return 


#for Option 4
def option4(search_name, task_id):
    for item in list_of_tasks:
        # 2. Check if the value associated with the 'name' key 
        #    matches the task_name the user provided.
        if item['name'] == search_name and task_id == item['id']: 
            # 3. If a match is found, return the task dictionary immediately.
            item['status'] = 'Completed'
            print(f"Task '{search_name}' is now completed!")

    return 


#For Option 5
def option5():
        save_tasks() 
        print("Exiting application. Goodbye!")
        return









#creating a main function
def main():
    print("Welcome to MiList")
    while True:
        print("\n***** To do List *****\n")
        print("1. Add a New Task")
        print("2. Show Task List")
        print("3. Start A Task")
        print("4. Mark a Task as Done")
        print("5. Exit")

        Choice = input("enter Your Choice:  ")
        if Choice == '1':
            task_name = input("enter task: ")
            option_1(task_name);

        elif Choice == '2':
            option2()

        elif Choice == '3':
            print("\n######### Search for Task #########")
            search_name = input("\nEnter Task Name: ")
            task_id = int(input("Enter unique Serial Number: "))
            if len(list_of_tasks) == 0: # This reads: "If NOT (the list is True/Non-empty)"
                print("The list is empty! Add a new task.")
            else:
                option3(search_name, task_id)
        
        elif Choice == '4':
            print("\n######### Search fo Task #########")
            search_name = input("\nEnter Task Name: ")
            task_id = int(input("Enter unique Serial Number: "))
            option4(search_name, task_id)

        elif Choice == '5':
            option5()
            break

        else:
            print("Wrong input...")

if __name__ == "__main__":
    load_tasks()
    main()





