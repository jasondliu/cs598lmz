import io
class File(io.RawIOBase):
	"""
	File is a wrapper for io.RawIOBase which allows for writing to a file
	without closing it
	"""
	def __init__(self, file):
		self.file = file
	def write(self, data):
		self.file.write(data)
	def read(self, size=-1):
		return self.file.read(size)
	def seek(self, offset, whence=io.SEEK_SET):
		self.file.seek(offset, whence)
	def close(self):
		pass

class Cursor(object):
	def __init__(self, file, offset):
		self.file = file
		self.offset = offset
	def __enter__(self):
		self.file.seek(self.offset)
	def __exit__(self, type, value, traceback):
		pass

class Base(object):
	def __init__(self, file, offset=0):
		self.file = File(file)
		self.offset = offset
	
