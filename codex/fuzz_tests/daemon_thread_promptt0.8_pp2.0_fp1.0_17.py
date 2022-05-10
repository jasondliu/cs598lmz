import threading
# Test threading daemon
class TestThread(threading.Thread):
    def __init__(self, id, name, delay):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name
        self.delay = delay
 
    def run(self):
        print "Starting " + self.name
        print_time(self.name, self.delay, 5)
        print "Exiting " + self.name
 
def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1
 
# Create new threads
thread1 = TestThread(1, "Thread-1", 1)
thread2 = TestThread(2, "Thread-2", 2)
 
# Start new Threads
thread1.start()
thread2.start()

#Test Multi-threading
# When main thread exit, the daemon threads will be killed as well.
# thread1.setDaemon(True)
