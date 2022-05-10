import threading
# Test threading daemon
class TestThread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		while True:
			print('Thread')

t1 = TestThread()
t1.setDaemon(True)
t1.start()

while True:
	print('Main')
	time.sleep(0.5)
