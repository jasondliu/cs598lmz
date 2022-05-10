import threading
# Test threading daemon process

import time
import threading

class MyThread(threading.Thread):
	"""docstring for MyThread"""
	def __init__(self, arg):
		super(MyThread, self).__init__()
		self.arg = arg

	def run(self):
		for i in range(5):
			print("job %s %d" %(self.arg, i))
			time.sleep(1)


def main():
	for i in range(3):
		t = MyThread(i)
		t.setDaemon(True)
		t.start()

	print("Main thread exit")

if __name__ == '__main__':
	main()
