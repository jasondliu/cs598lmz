import sys, threading

def run():
	l = [i for i in range(10)]
	for i in l:
		print(i)
		time.sleep(0.2)

# t = threading.Thread(target=run)
# t.start()
# while True:
# 	print("Main thread")
# 	time.sleep(0.2)

# class MyThread(threading.Thread):
# 	def __init__(self, name):
# 		super(MyThread, self).__init__()
# 		self.name = name
# 	def run(self):
# 		print("Thread %s is running..." % self.name)
# 		time.sleep(1)

# t1 = MyThread("t1")
# t1.start()

# t2 = MyThread("t2")
# t2.start()

import time
import threading

class MyThread(threading.Thread):
	def __init__(self, name):
		super(MyThread, self).__init__()

