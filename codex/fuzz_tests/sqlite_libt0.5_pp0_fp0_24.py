import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys

libc = ctypes.CDLL(ctypes.util.find_library('c'))

class Worker(threading.Thread):
    def __init__(self, task_id, worker_id, db_path, lock, tasks_done):
        super(Worker, self).__init__()
        self.task_id = task_id
        self.worker_id = worker_id
        self.db_path = db_path
        self.lock = lock
        self.tasks_done = tasks_done

    def run(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # fetch task
        cursor.execute("SELECT * FROM tasks WHERE id = ?", (self.task_id,))
        task = cursor.fetchone()

        # execute task
        print("[*] Worker %d: executing task %d" % (self.worker_id, self.task_id))
        libc.system(task[2])

        # update task
        cursor
