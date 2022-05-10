import threading
# Test threading daemon
# https://docs.python.org/3/library/threading.html#threading.Thread.setDaemon

def f():
    print('started')
    while True:
        print('hello')
        time.sleep(3)

t = threading.Thread(target=f)
t.start()
t.setDaemon(True)

# Other threading examples

# Threading is used to execute code concurrently by using multiple threads
# Threads are different than processes, they are more lightweight and share a lot of their resources

# The syntax for creating a thread is similar to that of a process, but we need to create a subclass from the Thread class and override the run method.

import threading
import time

class MyThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        
    def run(self):
        print('Starting: ', self.name)
        print_time
