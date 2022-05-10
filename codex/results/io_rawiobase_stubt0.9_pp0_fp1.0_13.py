import io
class File(io.RawIOBase):

	def __init__(self, wrappedfile):
		self.file = wrappedfile
		self.buffer = b''
		self.buffersize = 4096


	def read1(self, n=-1):
		return self.file.read1(n)

	def readable(self):
		return True

	def read(self, n=-1, ):
		# When EOF was reached, io.FILE objects return b'', io.BytesIO returns b''
		if self.buffer == b'' and not self.file.readable():
				return b''
		if len(self.buffer) < n:
				self.buffer += self.read1(self.buffersize)
		m = min(len(self.buffer), n)
		data, self.buffer = self.buffer[:m], self.buffer[m:]
		return data

	# TODO: add more read* functions when needed (readinto, readline)

# The fakeserial module is excellent, but it is a bit buggy when it comes
