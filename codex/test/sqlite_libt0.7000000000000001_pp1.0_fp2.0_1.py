import ctypes
import ctypes.util
import threading
import sqlite3
import os
import json
import shutil
import time
import math

# define mutex
mutex = threading.Lock()

# create thread class
class sqliteWorker(threading.Thread):
    
    # init method
    def __init__(self, threadID, name, conn, c):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.conn = conn
        self.c = c
    
    # run method
