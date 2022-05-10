import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os

class MyThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        print("Starting " + self.name)
        try:
            while True:
                #print("\n" + self.name + ": " + str(self.threadID) + " - " + str(time.ctime(time.time())))
                #time.sleep(10)
                #print("\n" + self.name + ": " + str(self.threadID) + " - " + str(time.ctime(time.time())))
                time.sleep(10)
        except KeyboardInterrupt:
            print("\n" + self.name + ": " + str(self.threadID) + " - " + str(time.ctime(time.time())))
        print("Exiting " + self.name)

class MyThread2(threading.
