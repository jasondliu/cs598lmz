import threading
# Test threading daemon
class TestThreadingDaemon(threading.Thread):
	def __init__(self, thread_id, name, counter):
		threading.Thread.__init__(self)
		self.thread_id = thread_id
		self.name = name
		self.counter = counter
	def run(self):
		print("Starting " + self.name)
		print_time(self.name, self.counter, 5)
		print("Exiting " + self.name)
def print_time(thread_name, delay, counter):
	while counter:
		time.sleep(delay)
		print("%s: %s" % (thread_name, time.ctime(time.time())))
		counter -= 1
thread1 = TestThreadingDaemon(1, "Thread-1", 1)
thread2 = TestThreadingDaemon(2, "Thread-2", 2)
thread1.start()
thread2.start()
print("Exiting Main Thread")

# Test threading lock
class TestThreadingLock(threading
