import threading
# Test threading daemon mode

class daemon_thread(threading.Thread):

	def __init__(self):
		threading.Thread.__init__(self)
		self.daemon = True
		self.start()
	
	def run(self):
		for i in range(10):
			print("daemon ",i)
			time.sleep(1)
	
		print("daemon thread end")

dt = daemon_thread()
time.sleep(1)

print("main thread end")

# Test threading wait

class thread_with_waiting(threading.Thread):

	def __init__(self, cond, count):
		threading.Thread.__init__(self)
		self.cond = cond
		self.count = count
		self.daemon = True
		self.start()

	def run(self):
		self.cond.acquire()
		self.cond.wait()
		print("I got {}".format(self.count))
		self.cond.
