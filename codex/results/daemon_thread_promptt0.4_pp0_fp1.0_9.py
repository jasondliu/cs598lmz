import threading
# Test threading daemon

class MyThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        print "Starting " + self.name
        print_time(self.name, 5, self.threadID)
        print "Exiting " + self.name

def print_time(threadName, counter, delay):
    while counter:
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1

# Create new threads
thread1 = MyThread(1, "Thread-1")
thread2 = MyThread(2, "Thread-2")

# Start new Threads
thread1.start()
thread2.start()

print "Exiting Main Thread"

# Test threading daemon

class MyThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.
