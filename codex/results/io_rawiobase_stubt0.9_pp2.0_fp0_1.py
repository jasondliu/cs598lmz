import io
class File(io.RawIOBase):
	def __init__(self, name, mode="rb"):
		self.name = name
		self.mode = mode

	def readable(self):
		return self.mode in ("r", "w+", "r+", "x+", "a+")

	def writable(self):
		return self.mode in ("w", "w+", "r+", "x+", "a+")

	@property
	def isatty(self):
		return False

	@property
	def closed(self):
		return False

	def close(self):
		pass

	def closefd(self):
		pass

	def fileno(self):
		return 0

	def flush(self):
		pass

	def seekable(self):
		return True

	def seek(self, pos, whence=io.SEEK_SET):
		pass

	def tell(self):
		pass

	def truncate(self,  size=None):
		pass

	def writelines(self, lines):

