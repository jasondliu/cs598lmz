import io
class File(io.RawIOBase):
	_chunk_size = 512 # in bytes
	def __init__(self,file_path):
		if not os.path.exists(file_path):
			sys.stderr.write(file_path+' does not exist\n')
			sys.exit(1)
		self.file_path = file_path
		self.file_size = os.path.getsize(file_path)
		self.position = 0

	def read(self,size=-1):
		if size < 0:
			size = self.file_size
		with open(self.file_path,'rb') as file:
			file.seek(self.position)
			self.position += size
			data = file.read(size)
		return data

	def readable(self):
		return True

	def readinto(self,b):
		data = self.read(len(b))
		n = len(data)
		try:
			b[:n
