# FinalProject.py
# Copyright © 2024 - Cleo Naughton. All rights reserved.
# Introduction to Programming: Python I at Evergreen State College Fall 2024.
# Final Project: Task Manager Application

# ANSI escape codes for colored text
# https://en.wikipedia.org/wiki/ANSI_escape_code#SGR
RED = "\033[91m"
GREEN = "\033[92m"
WHITE = "\033[97m"
BLUE = "\033[94m"

# Preparing the menu function with the array of menu items
def menu():
  items = ["Add Task", "Mark Tasks as Complete", "View Tasks", "Delete Task", "Filter Tasks", "Exit"]
  counter = 1
  for item in items:
    print(f"{RED}{counter}. {GREEN}{item}")
    counter += 1

# Task class - holds description and completion status of a task
class Task:
  # The initializer sets description and completed to false
  def __init__(self, description):
    self.description = description
    self.completed = False
  # A method to set completed to true
  def complete(self):
    self.completed = True

# List of tasks - pre-populated with three demo tasks
tasks = [Task("Buy groceries"), Task("Do laundry"), Task("Clean the house")]

# Functions to implement the six menu choices

# 1. Function to add a task to the list
def addTask():
  # Print a formatted prompt and stores user input into description var
  description = input(f"\n{RED}Enter task description: {GREEN}")
  # Creates new task with description, and append to tasks list
  tasks.append(Task(description))
  print(f"{GREEN}Task added successfully!")
 
# 2. Mark task as complete.
def completeTask():
  taskNumber = input(f"\n{RED}Enter task number to mark as complete: {GREEN}")
  # Convert string to integer
  taskNumber = int(taskNumber)
  # Subtract one from taskNumber because the first task is 1 in the UI and 0 in the array.
  tasks[taskNumber - 1].complete()
  print(f"{GREEN}Task {taskNumber} marked as complete!\n")

# 3. View all tasks
def viewTasks():
  counter = 1
  for task in tasks:
    # Checks if task is complete or not based on if its completed, respond accordingly.
    if (task.completed):
      completedOrNot = f"{WHITE}[{GREEN}Complete{WHITE}] "
    else:
      completedOrNot = ""
    print(f"{RED}{counter}. {completedOrNot}{GREEN}{task.description}")
    counter += 1

# 4. Delete a task
def deleteTask():
  taskNumber = input(f"\n{RED}Enter task number to delete: {GREEN}")
  taskNumber = int(taskNumber)
  # Remove task from tasks array.
  del tasks[taskNumber - 1]
  print(f"{GREEN}Task {taskNumber} deleted successfully!\n") 
 
# 5. View tasks filtered by completion status
def filterTasks():
  print(f"{RED}Filter by:")
  print(f"{RED}1{GREEN}. Complete tasks")
  print(f"{RED}2{GREEN}. Incomplete tasks")
  
  choice = input(f"\n{RED}Enter your choice: {GREEN}")
  choice = int(choice)
  counter = 1
  for task in tasks:
    # Boolean expression to determine whether or not to print the task.
    # If user input specified complete, show complete, and vice versa.
    if (task.completed and choice == 1) or (not task.completed and choice == 2):
      print(f"{RED}{counter}{GREEN}. {task.description}")
      counter += 1
  # Counter = 1 when no items were printed above.
  if counter == 1:
    # Set word to complete or incomplete based on user input.
    if choice == 1: 
      word = "complete"
    else:
      word = "incomplete"
    print(f"{BLUE}No {GREEN}{word} tasks found.\n")

# main loop
print(f"{GREEN}Welcome to the Task Manager Application!\n")
menu()
done = False
# Create loop that runs until done = true.
while not done:  
  choice = input(f"\n{RED}Please enter your choice: ")
  if choice == "1":
    addTask()
  elif choice == "2":
    completeTask()
  elif choice == "3":
    viewTasks()
  elif choice == "4":
    deleteTask()
  elif choice == "5":
    filterTasks()
  elif choice == "6":
    print(f"{GREEN}Thank you for using the Task Manager Application!")
    # Close loop.
    done = True
  else:
    menu()