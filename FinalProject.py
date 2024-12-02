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

def menu():
  items = ["Add Task", "Mark Tasks as Complete", "View Tasks", "Delete Task", "Filter Tasks", "Exit"]
  counter = 1
  for item in items:
    print(f"{RED}{counter}. {GREEN}{item}")
    counter += 1

# Task class - holds description and completion status of a task
class Task:
  def __init__(self, description):
    self.description = description
    self.completed = False
  def complete(self):
    self.completed = True

# List of tasks - pre-populated with three demo tasks
tasks = [Task("Buy groceries"), Task("Do laundry"), Task("Clean the house")]

def addTask():
  description = input(f"\n{RED}Enter task description: {GREEN}")
  tasks.append(Task(description))
  print(f"{GREEN}Task added successfully!")
 
def completeTask():
  print("completeTask")
  
def viewTasks():
  counter = 1
  for task in tasks:
    print(f"{RED}{counter}. {GREEN}{task.description}")
    counter += 1
  
def deleteTask():
  print("del")
  
def filterTasks():
  print("filter")
    





# main loop
print(f"{GREEN}Welcome to the Task Manager Application!\n")
menu()
done = False
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
    print("Thank you for using the Task Manager Application!")
    done = True
  else:
    menu()