# FinalProject.py
# Copyright © 2024 - Cleo Naughton. All rights reserved.
# Introduction to Programming: Python I at Evergreen State College Fall 2024.
# Final Project: Task Manager Application

def menu():
  items = ["Add Task", "Mark Tasks as Complete", "View Tasks", "Delete Task", "Filter Tasks", "Exit"]
  counter = 1
  for item in items:
    print(f"{counter}. {item}")
    counter += 1

def addTask():
  print("add task")
  
def completeTask():
  print("completeTask")
  
def viewTasks():
  print("lookem")
  
def deleteTask():
  print("del")
  
def filterTasks():
  print("filter")
    





# main loop
print("Welcome to the Task Manager Application!\n")
menu()
done = False
while not done:  
  choice = input("\nPlease enter your choice: ")
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