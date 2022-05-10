import threading
# Test threading daemon.

def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (threadName, time.ctime(time.time())))

# Create two threads as follows
try:
    threading.Thread(target=print_time, args=("Thread-1", 2, )).start()
    threading.Thread(target=print_time, args=("Thread-2", 4, )).start()
except:
    print("Error: unable to start thread")

while 1:
    pass
# This is a simple example of the threading module.

import threading

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("Starting " + self.name)
        # Get lock to synchronize threads
