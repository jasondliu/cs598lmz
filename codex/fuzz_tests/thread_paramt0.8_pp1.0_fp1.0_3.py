import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello from thread A\n")).start()
threading.Thread(target=lambda: sys.stdout.write("Hello from thread B\n")).start()
print("Hello from main thread.")

print('\nthreading module - an example')
import threading

class MyThread(threading.Thread):
	def run(self):
		print("{} has started!".format(self.getName())) #thread name
		try:
			if self._target:
				self._target(*self._args, **self._kwargs)
		finally:
			del self._target, self._args, self._kwargs
		print("{} has finished!".format(self.getName()))

def double(number, cycles):
	for i in range(cycles):
		number += number
	print(number)

threads_list = [MyThread(target=double, args=(2, 10)) for i in range(5)]
for t in threads_list:
	t.start()

