import io
class File(io.RawIOBase):
	def __init__(self, file):
		self.file = file
	def read(self, n=10000):
		if n > 0:
			return self.file.read(min(n, len(self)-self.tell()))
		else:
			return b""
	def seek(self, offset, whence=io.SEEK_SET):
		self.file.seek(offset, whence)
	def tell(self):
		return self.file.tell()
	def readable(self):
		return True
	def writable(self):
		return False
	def seekable(self):
		return True
	def close(self):
		self.file.close()
	def __len__(self):
		position = self.file.tell()
		self.file.seek(0, io.SEEK_END)
		value = self.file.tell()
		self.file.seek(position, io.SEEK_SET)
		return value
