import io
class File(io.RawIOBase):

	def __init__(self, filename=None , mode='r', buffering=-1):
		if filename is not None:
			if mode in ('r', 'rb') :
				self.readMode = True
		self.buffer = StringIO()
		self.encoding = 'utf-8'
		self.newlines = ['\n']

		self.mode = mode

		self.name = filename
		self.closed = False


	def read(self, n=None):
		return self.buffer.read(n)

	def write(self, s):
		if self.readMode:
			raise Exception("file was opened for reading, can't write")
		self.buffer.write(s)
		return len(s)

	def readable(self):
		return True


	def writable(self):
		return True

	def seekable(self):
		return True

	def seek(self, position, whence=0):
		if whence == 0:
		
