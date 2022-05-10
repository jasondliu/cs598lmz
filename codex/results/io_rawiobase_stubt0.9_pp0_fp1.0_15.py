import io
class File(io.RawIOBase):
	def __init__(self,filename, mode = 'r'):
		self._file = None
		self._filename = filename
		self._mode = mode
	def fileno(self):
		return self._file.fileno()
	def close(self):
		self._file.close()
	def readinto(self, b):
		return self._file.readinto(b)
	def read(self,*args) :
		return self._file.read(*args)
	def write(self,data):
		#if self._mode == 'r' :
		#	raise Exception('file can not write to read-file')
		self._file.write(data)
	def seekable(self):
		return self._file.seekable()
	def seek(self,*args) :
		return self._file.seek(*args)
	def tell(self):
		return self._file.tell()
	def readline(self):
		return self._file.readline()
	def writeable(
