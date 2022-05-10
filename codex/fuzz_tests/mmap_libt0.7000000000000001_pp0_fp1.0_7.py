import mmap
import sys

def open_file():
    filename = input("Enter file name: ")
    try:
        f = open(filename, "r+b") #open file
        return f
    except FileNotFoundError:
        print("File not found.")
        sys.exit()

def get_tasks(f):
    tasks = []
    for line in f:
        task = str(line)
        task = task.rstrip()
        tasks.append(task)
    return tasks

def get_completed(f):
    tasks = get_tasks(f)
    completed = []
    for i in range(len(tasks)):
        if tasks[i][0] == "1":
            completed.append(tasks[i])
    return completed

def get_uncompleted(f):
    tasks = get_tasks(f)
    uncompleted = []
    for i in range(len(tasks)):
        if tasks[i][0] == "0":
            uncompleted.append(tasks[i])
    return
