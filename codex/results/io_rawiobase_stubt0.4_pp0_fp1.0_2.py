import io
class File(io.RawIOBase):
	def __init__(self, file, mode='rb', closefd=True):
		self._file = file
		self._mode = mode
		self._closefd = closefd
		self._pos = 0
	def read(self, size=-1):
		if size < 0:
			return self._file.read()
		else:
			return self._file.read(size)
	def tell(self):
		return self._pos
	def seek(self, offset, whence=0):
		if whence == 0:
			self._pos = offset
		elif whence == 1:
			self._pos += offset
		elif whence == 2:
			self._pos = self._file.seek(0, 2) + offset
		else:
			raise ValueError('Invalid value for whence')
		self._file.seek(self._pos)
		return self._pos
	def close(self):
		if self._closefd:
			self._file.close
