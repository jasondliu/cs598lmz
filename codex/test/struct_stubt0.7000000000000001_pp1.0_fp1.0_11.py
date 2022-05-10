from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')

class MemoryStream:
	def __init__(self, data=""):
		self.data = data
		self.pos = 0

	def seek(self, pos):
		self.pos = pos

	def read(self, size):
		self.pos += size
		return self.data[self.pos - size : self.pos]

	def readInt(self):
		return s.unpack(self.read(4))[0]
	
	def readString(self):
		return self.read(self.readInt())

	def writeInt(self, value):
		self.data += s.pack(value)

	def writeString(self, value):
		self.writeInt(len(value))
		self.data += value

	def getvalue(self):
		return self.data

class MemoryFile(MemoryStream):
	def __init__(self, data=""):
		MemoryStream.__init__(self, data)
