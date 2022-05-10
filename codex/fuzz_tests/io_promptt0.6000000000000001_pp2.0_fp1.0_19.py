import io
# Test io.RawIOBase
# Test io.BufferedIOBase

class MyRawIO(io.RawIOBase):
	def __init__(self, data):
		self.data = data
		self.pos = 0
	def read(self, n=-1):
		if n < 0:
			newpos = len(self.data)
		else:
			newpos = min(self.pos+n, len(self.data))
		r = self.data[self.pos:newpos]
		self.pos = newpos
		return r
	def write(self, b):
		data = self.data
		if self.pos >= len(data):
			data += b
		else:
			data = data[:self.pos] + b + data[self.pos+len(b):]
		self.data = data
		self.pos += len(b)
	def seek(self, pos, whence=0):
		if whence == 0:
			self.pos = pos

