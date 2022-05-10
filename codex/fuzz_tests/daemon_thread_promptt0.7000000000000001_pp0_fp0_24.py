import threading
# Test threading daemon

import time

class WorkerThread(threading.Thread):
    def __init__(self, name):
        super(WorkerThread, self).__init__()
        self.name = name
        self.daemon = True

    def run(self):
        print "My Thread name is: " + self.name
        for i in range(2):
            time.sleep(0.5)
            print "Thread {0}: Hello world".format(self.name)

for i in range(3):
    t = WorkerThread(str(i))
    t.start()
print "Main thread is finished"

# Test threading lock

import threading
import time

class Account(object):

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self, money):
        self.lock.acquire()
        try:
            new_balance = self.balance + money
            time.sleep(0.01)
            self.balance = new_balance
        finally:
            self.lock
