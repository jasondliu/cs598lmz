import socket
import sys
import time
import random
import threading

class myworker(threading.Thread):
	def __init__(self, generator, func, events):
		"""
		generator: a generator function which can iterate the tasks
		func: handle for every task
		events: a list of event for each task
		"""
		super(myworker, self).__init__()
		self.generator = generator
		self.func = func
		self.events = events
		
		for e in self.events:
			e.clear()

	def run(self):
		for pair in self.generator():
			self.func(pair)
			e = self.events[pair[0]]
			with e:
				e.notify()
		
def random_sleep():
	time.sleep(random.uniform(0, 5))

def f(pair):
	i = pair[0]
	s = pair[1]
	print 'handle socket
