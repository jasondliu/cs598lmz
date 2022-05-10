import ctypes
import ctypes.util
import threading
import sqlite3

tasksdb = "tasks.db"

def main():
    tasks_connect = sqlite3.connect(tasksdb)
    tasks_cursor = tasks_connect.cursor()
    tasks_cursor.execute("CREATE TABLE IF NOT EXISTS tasks (task TEXT)")
    tasks_connect.commit()
    tasks_cursor.execute("SELECT * FROM tasks")
    tasks = tasks_cursor.fetchall()
    c_user32 = ctypes.CDLL(ctypes.util.find_library("user32"))
    ids = []
    thread_list = []
    for task in tasks:
        thread = threading.Thread(target=popup_message,args=(0,task[0],ids,c_user32))
        thread.start()
        thread_list.append(thread)
        #popup_message(0,task[0],ids,c_user32)
    for thread in thread_list:
        thread.join()

def popup_message(flags, text, ids, c_user32):
    c
