import threading
# Test threading daemon
def target():
    global check
    while not check:
        threadLock.acquire(1)
        print("I am alive")
        threadLock.release()
    print("Leave the loop")

# Now using threading
class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("Starting thread " + self.name)
        print_count(self.name, self.counter, 5)

def print_count(threadName, delay, counter):
	while counter:
		if exitFlag:
			threadName.exit()
		time.sleep(delay)
		print("%s: %s" % (threadName, time.ctime(time.time())))
		counter -= 1

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(
