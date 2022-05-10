import io
class File(io.RawIOBase):
	def __init__(self, file):
		self.file = file
		self.offset = 0
	def readable(self):
		return True
	def writable(self):
		return False
	def seekable(self):
		return True
	def readinto(self, b):
		self.file.seek(self.offset)
		l = self.file.readinto(b)
		self.offset += l
		return l
	def seek(self, offset, whence=io.SEEK_SET):
		if whence == io.SEEK_SET:
			self.offset = offset
		elif whence == io.SEEK_CUR:
			self.offset += offset
		elif whence == io.SEEK_END:
			self.offset = len(self.file.read()) + offset
		return self.offset
	def tell(self):
		return self.offset

class StringIO(io.RawIOBase):
	def __init__(self, initial_bytes
