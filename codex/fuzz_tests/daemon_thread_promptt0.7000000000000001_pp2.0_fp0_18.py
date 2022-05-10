import threading
# Test threading daemon
from time import sleep

class myThread(threading.Thread):
    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        self.threadID = counter
        self.name = name
        self.counter = counter
    def run(self):
        print("Starting " + self.name, end='\r')
        print_time(self.name, 5, self.counter)
        print("Exiting " + self.name, end='\r')

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())), end="\r")
        counter -= 1

# Create new threads
thread1 = myThread("Thread-1", 1)
thread2 = myThread("Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

print("Exiting Main Thread", end='\r')


# Copyright (c) 2017,
