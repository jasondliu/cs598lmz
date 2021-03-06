import threading
# Test threading daemon

class mythread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("Starting " + self.name)
        print_time(self.name, 5, self.counter)
        print ("Exiting " + self.name)

def print_time(threadName, counter, delay):
    while counter:
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

# Create new threads
thread1 = mythread(1, "Thread-1", 1)
thread2 = mythread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

thread1.join()
thread2.join()
print ("Exiting Main Thread")

# Test threading with lock
class mythread
