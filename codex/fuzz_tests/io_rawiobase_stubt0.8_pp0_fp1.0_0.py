import io
class File(io.RawIOBase):
	"""A raw file implement,at present ,it just provide read and readinto"""
	
	def __init__(self,name):
		self._fd = os.open(name,os.O_RDONLY)
	
	def read(self,size=-1):
		return os.read(self._fd,size)
	
	def readinto(self,b):
		return os.readinto(self._fd,b)

	def __del__(self):
		self.close()
	
	def close(self):
		os.close(self._fd)

class FileWithBuf(File):
	"""file with buf, size is the buffer size."""
	def __init__(self,name,size=4096):
		super().__init__(name)
		self._buf = bytearray(size)
		self._len = len(self._buf)
		self._pos = 0
		self._end = 0
		self._fill_buffer(size)
	
	def _fill_
