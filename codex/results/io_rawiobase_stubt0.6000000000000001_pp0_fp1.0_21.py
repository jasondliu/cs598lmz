import io
class File(io.RawIOBase):
	def __init__(self, file):
		self.file = file
		self.pos = 0
		self.buf = b''
		self.length = self.file.length
	def readable(self):
		return True
	def seekable(self):
		return True
	def seek(self, offset, whence=0):
		if whence == io.SEEK_SET:
			self.pos = offset
		elif whence == io.SEEK_CUR:
			self.pos += offset
		elif whence == io.SEEK_END:
			self.pos = self.length + offset
		return self.pos
	def tell(self):
		return self.pos
	def read(self, size=None):
		if size is None:
			size = self.length - self.pos
		curpos = self.pos
		self.pos += size
		if self.pos > self.length:
			size -= self.pos-self.length
	
