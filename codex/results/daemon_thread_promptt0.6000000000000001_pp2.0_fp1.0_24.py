import threading
# Test threading daemon.
import time

class T(threading.Thread):
	def __init__(self, name):
		threading.Thread.__init__(self)
		self.name = name

	def run(self):
		for i in range(6):
			print("Thread [%s] says: %s" % (self.name, i))
			time.sleep(1)

t1 = T("thread1")
t1.setDaemon(True)
t1.start()

print("Main thread says: %s" % (1))
time.sleep(0.5)
print("Main thread says: %s" % (2))
time.sleep(0.5)
print("Main thread says: %s" % (3))
time.sleep(0.5)
print("Main thread says: %s" % (4))
time.sleep(0.5)
print("Main thread says: %s" % (5))
time.sleep(0.5)
print("Main thread says: %s" % (6))
time
