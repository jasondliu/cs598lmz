import io
class File(io.RawIOBase):
	def __init__(self,path):
		self.path = path
		self.file = None
	def readable(self):
		return True
	def writable(self):
		return True
	def seekable(self):
		return True
	def seek(self,offset,whence=io.SEEK_SET):
		self.file.seek(offset,whence)
	def tell(self):
		return self.file.tell()
	def write(self,b):
		self.file.write(b)
	def readinto(self,b):
		return self.file.readinto(b)
	def read(self,size=-1):
		return self.file.read(size)
	def close(self):
		self.file.close()
	def open(self,mode):
		self.file = open(self.path,mode)
	def __enter__(self):
		self.open('+ab')
		return self
	def __exit__(self,type,
