import io
class File(io.RawIOBase):
	"""
	File abstraction class.
	"""
	def __init__(self,file_name,mode):
		super(File,self).__init__()
		self.proper_file = open(file_name,mode)
		self.read_byte_func = self.proper_file.read
		self.write_byte_func = self.proper_file.write
		self.set_proper_read_byte()
		self.set_proper_write_byte()
		self.set_proper_read_stream()
		self.set_proper_write_stream()
		self.set_proper_read()
		self.set_proper_write()
		self.set_proper_seek()
		self.set_proper_tell()
		self.set_proper_close()
	def set_proper_read_byte(self):
		self.read_byte = self.read_byte_func
	def set_proper_write_byte(self):
