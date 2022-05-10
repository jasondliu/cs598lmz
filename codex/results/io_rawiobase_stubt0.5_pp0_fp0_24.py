import io
class File(io.RawIOBase):
	def __init__(self, fname):
		self.fname = fname
		self.f = None
	def __enter__(self):
		self.f = open(self.fname, 'rb')
		return self
	def __exit__(self, *args):
		self.close()
	def read(self, n=-1):
		if self.f is None:
			raise ValueError("I/O operation on closed file")
		return self.f.read(n)
	def close(self):
		if self.f is not None:
			self.f.close()
			self.f = None
	def readable(self):
		return True
	def seekable(self):
		return True
	def writable(self):
		return False
	def seek(self, offset, whence=0):
		if self.f is None:
			raise ValueError("I/O operation on closed file")
		return self.f.seek(offset, whence
