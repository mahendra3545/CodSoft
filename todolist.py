'''Date: 18 November 2023
Author:Mahendra pratap singh
Programme: To-do list to keep track task'''
import os
#defining task function
#takin input from user
def create_task():
    task_name = input("Enter task name: ")
    task_description = input("Enter task description: ")
    task_priority = input("Enter task priority (high, medium, low): ")
    task = {
        "name": task_name,
        "description": task_description,
        "priority": task_priority,
        "status": "incomplete"
    }
    return task
#function for updating task
def view_tasks():
    with open("tasks.txt", "r") as tasks_file:
        tasks = tasks_file.read().splitlines()
        for task in tasks:
            print(task)
def update_task():
    task_name = input("Enter task name to update: ")
#task status complete or incomplete
    new_status = input("Enter new task status (complete, incomplete): ")
    with open("tasks.txt", "r") as tasks_file:
        tasks = tasks_file.read().splitlines()
    for task in tasks:
        if task.startswith(task_name):
            new_task = task.replace("incomplete", new_status)
            tasks.remove(task)
            tasks.append(new_task)
    with open("tasks.txt", "w") as tasks_file:
        tasks_file.write("\n".join(tasks))
#input choice from user
def main():
    choice = input("""
        To-Do List Menu:
        1. Create Task
        2. View Tasks
        3. Update Task
        4. Exit
        Enter your choice: """)
    while choice != "4":
        if choice == "1":
            task = create_task()
            with open("tasks.txt", "a") as tasks_file:
                tasks_file.write(f"{task['name']}:\n {task['description']}, {task['priority']}, {task['status']}\n")
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        else:
            print("Invalid choice. Please try again.")
        choice = input("\nEnter your choice: ")
    print("Goodbye!\n")
if __name__== "_main_":
   main()