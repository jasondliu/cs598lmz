import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print "Starting " + self.name
        # Get lock to synchronize threads
        #threadLock.acquire()
        #print_time(self.name, self.counter, 3)
        try:
            sqlite3.connect(self.name)
        except sqlite3.OperationalError as e:
            print "Error in Thread ID:", self.threadID, "; Error:", e
        # Free lock to release next thread
        #threadLock.release()

def print_time(threadName, counter, delay):
    while counter:
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1

threadLock = threading.Lock()
threads = []

