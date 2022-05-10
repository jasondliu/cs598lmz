import io
class File(io.RawIOBase):
	"""
	File class.
	"""
	def read(self, size):
		"""
		Reads and returns the specified number of bytes from the file.
		
		If the specified number of bytes could not be read, then an
		empty bytes object is returned.
		"""
		raise NotImplementedError()
	
	def readinto(self, buf):
		"""
		Reads from the file into the given buffer.
		
		The buffer is not cleared before reading into it, so the data
		will be appended to the end of the buffer.
		
		Returns the number of bytes read, or 0 if no bytes could be read.
		"""
		raise NotImplementedError()
	
	def readline(self, size=-1):
		"""
		Reads and returns one line from the file.
		
		If size is specified, at most size bytes will be read.
		
		If a line could not be read, then an empty bytes object is
		returned.
