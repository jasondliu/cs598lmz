import threading
# Test threading daemon
class mythread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name


    def run(self):
        print("Starting " + self.name)
        time.sleep(1)
        print("Exiting " + self.name)

print("Creating threads")

thread1 = mythread("Thread-1")
thread2 = mythread("Thread-2")

thread1.setDaemon(True)
thread2.setDaemon(True)

thread1.start()
thread2.start()

print("Exiting main thread")

# Queue
print("Single thread threading")

import queue
import threading
import time

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        print
