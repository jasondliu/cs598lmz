import select
import time
import os

class pipe():
	def __init__(self):
		self.fifo = "/tmp/mypipe"
		self.fifo_mode = "r"
		self.fifo_size = 1024
		self.init()

	def init(self):
		if not os.path.exists(self.fifo):
			os.mkfifo(self.fifo)

	def read(self):
		fifo = open(self.fifo, self.fifo_mode)
		val = fifo.read(self.fifo_size)
		fifo.close()
		return val

	def write(self, data):
		fifo = open(self.fifo, self.fifo_mode)
		fifo.write(data)
		fifo.close()


def main():
	p = pipe()
	while True:
		data = p.read()
		print data

if __name__ == '__main__':
	main()
