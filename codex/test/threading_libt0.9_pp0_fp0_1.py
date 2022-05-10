import threading
threading.stack_size(2**20 + 2**19)

from multiprocessing import Process
import signal

from traceback import format_exc
import sys

def getBatch(data, batchSize):
	return [data.pop() for _ in range(batchSize)]

class Worker(Process):

	def __init__(self, workerID, config, data):
		Process.__init__(self)
		self.workerID = workerID
		self.config = config
		self.data = data

	def addData(self, data):
		pass

	def run(self):
		pass

# A worker that is processing multiple batches at the same time.
class BatchWorker(Worker):

	def __init__(self, workerID, config, data):
		Worker.__init__(self, workerID, config, data)
		self.batches = []
		self.batchTerminated = {}

	def addData(self, data):
		self.data.extend(data)

