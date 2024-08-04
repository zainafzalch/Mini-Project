# Project Requirements

#     User Interface (UI):

#         Create a command-line interface (CLI) for the To-Do List Application.

#         Display a welcoming message and a menu with the following options:

#                 Welcome to the To-Do List App!

#                 Menu:
#                 1. Add a task
#                 2. View tasks
#                 3. Mark a task as complete
#                 4. Delete a task
#                 5. Quit

#     To-Do List Features:

#         Implement the following features for the To-Do List:

#             Adding a task with a title (by default “Incomplete”).

#             Viewing the list of tasks with their titles and statuses (e.g., "Incomplete" or "Complete").

#             Marking a task as complete.

#             Deleting a task.

#             Quitting the application.

#     User Interaction:

#         Allow users to interact with the application by selecting menu options using input().

#         Implement input validation to handle unexpected user input gracefully.

#     Error Handling:

#         Implement error handling using try, except, else, and finally blocks to handle potential issues.

#     Code Organization:

#         Organize your code into functions to promote modularity and readability.

#         Use meaningful function names with appropriate comments and docstrings for clarity.

#     Testing and Debugging:

#         Thoroughly test your application to identify and fix any bugs.

#         Consider edge cases, such as empty task lists or incorrect user input.

#     Documentation:

#         Include a README file that explains how to run the application and provides a brief overview of its features.


incomplete_tasks = []
completed_tasks = []

while(True):
    print("""
        Menu:
            1. Add a task
            2. View tasks
            3. Mark a task as complete
            4. Delete a task
            5. Quit
    """)

    try:
        action = int(input("Specify action by number: "))
    except ValueError:
        print("Action must be a number, Try Again! \n")
    else:
        match (action):

            case 1:
                task_to_add = input("Task Description: ").lower()
                incomplete_tasks.append(task_to_add)
            
            case 2:
                view_tasks() 

            case 3:
                mark_task_complete()

            case 4:
                task_to_remove()

            case 5:
                print("GOODBYE!")
                incomplete_tasks.clear()
                completed_tasks.clear()
                break

    def view_tasks():
        if(len(incomplete_tasks) == 0):
            print("No Incomplete Tasks!")
        else:
            for iteration, incomp_task in enumerate(incomplete_tasks):
                print(f'{iteration+1}: {incomp_task.capitalize()} | Status: Incomplete')
            print("\n-----------------------------------")
                    
        if(len(completed_tasks) == 0):
            print("No Completed Tasks!")
        else:
            for iteration, comp_task in enumerate(completed_tasks):
                print(f'{iteration+1}: {comp_task.capitalize()} | Status: Complete')

    def mark_task_complete():
        if(len(incomplete_tasks) == 0):
            print("There are no incomplete tasks")
        else:
            for item in incomplete_tasks:  
                print(item.capitalize())
            task_to_mark_completed = input("Enter task to mark as completed: ").lower()
            for incompleted_task in incomplete_tasks:
                if(incompleted_task == task_to_mark_completed):
                    completed_tasks.append(incompleted_task)
                    incomplete_tasks.remove(incompleted_task)

    def task_to_remove():
        list_to_remove_tasks_from = input("Completed or Incompleted task to remove: ").lower()
        if(list_to_remove_tasks_from == "completed"):
            for tasks in completed_tasks:
                print(tasks.capitalize())
            remove_task = input("Specify task to remove: ").lower()
            completed_tasks.remove(tasks)
        else:
            for tasks in incomplete_tasks:
                print(tasks.capitalize())
            remove_task = input("Specify task to remove: ").lower()
            incomplete_tasks.remove(remove_task)