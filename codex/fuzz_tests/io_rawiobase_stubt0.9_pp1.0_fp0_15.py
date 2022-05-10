import io
class File(io.RawIOBase):
	def __init__(self, name):
		self.file=mmap.mmap(-1,BUFSIZE,name,'r+',mmap.ACCESS_SHARED)
	def readinto(self, b):
		n=self.file.readinto(b)
		return n
	def read(self, n=-1):
		"""Read and return up to n bytes.
		If the argument is omitted, None, or negative, data is read and returned until EOF is reached."""
		return self.file.read(n)
	def write(self, b):
		"""Write the given bytes or bytearray object, b, to the underlying raw
		stream and return the number of bytes written.
		"""
		self.file.write(b)
		#print(self.file.buf)
		return len(b)
	def flush(self):
		"""Flush write buffers, if applicable.  This is not implemented for read-only and non-blocking streams."""
		self.file.flush()
