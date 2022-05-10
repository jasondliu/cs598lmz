import ctypes
import ctypes.util
import threading
import sqlite3
import time
import sys

class Sqlite3Thread(threading.Thread):
    def __init__(self, init, work):
        threading.Thread.__init__(self)
        self.sqlite3 = sqlite3
        self.busy = False
        self.init = init
        self.work = work
        self.result_queue = queue.Queue()
        self.start()

    def __del__(self):
        self.result_queue.put(None)
        self.join()

    def run(self):
        while True:
            init = self.init()
            if not init:
                break
            conn = self.sqlite3.connect(':memory:')
            conn.text_factory = str
            c = conn.cursor()
            for row in c.execute(init):
                pass
            conn.commit()
            self.busy = True
            while True:
                work = self.work()
                if not work:
                    break
                result = []
                for row in c.execute(work):

