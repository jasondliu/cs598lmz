import mmap
import os

class MemoryMap(object):
	"""
	"""
	def __init__(self, file_name):
		"""
		"""
		self.file_name = file_name
		self.file_handler = None
		self.mmap = None
		self.size = os.path.getsize(self.file_name)
		self.start = 0
		self.end = self.size
		self.last_offset = 0 

	def get_handler(self):
		if self.file_handler is None:
			self.file_handler = open(self.file_name, "r+b")
		return self.file_handler

	def get_mmap(self):
		if self.mmap is None:
			self.mmap = mmap.mmap(self.get_handler().fileno(), self.size, access=mmap.ACCESS_READ|mmap.ACCESS_WRITE)
		return self.mmap

	def __iter__(self
