import mmap
import random
import sys
import re

MMAP_LIMIT = 256*1024*1024
CHECK_INDEX = slice(12345, 12349)

class SeekableFile:
	def __init__(self, filename, mode=mmap.ACCESS_COPY):
		self.file = open(filename, 'r+b')
		self.mmap = mmap.mmap(self.file.fileno(), 0, access=mode)

	def write_bytes(self, offset, data):
		if offset+len(data) > self.mmap.size():
			padding = MMAP_LIMIT - (self.mmap.size() % MMAP_LIMIT)
			self.mmap.resize(self.mmap.size() + padding + len(data))
			#self.mmap.flush()
			self.mmap.seek(offset)
		else:
			self.mmap.seek(offset)

		self.mmap.write(data)

	def write
