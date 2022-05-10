import io
class File(io.RawIOBase):
	def __init__(self, filename, mode):
		self._fd = open(filename, mode)
		self._fd.read()
		self._fd.seek(0)
	
	def read(self, size=-1):
		return self._fd.read(size)
	
	def write(self, b):
		self._fd.write(b)
	
	def seek(self, offset, whence=0):
		self._fd.seek(offset, whence)
	
	def seekable(self):
		return True
	
	def readable(self):
		return True
	
	def writable(self):
		return True
	
	def close(self):
		self._fd.close()

def get_files(path, ext=None):
	files = []
	for file in os.listdir(path):
		if os.path.isfile(os.path.join(path, file)):
			if ext is None or file.endswith(ext):
			
