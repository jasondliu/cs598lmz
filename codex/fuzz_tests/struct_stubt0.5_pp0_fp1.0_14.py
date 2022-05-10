from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i'
s.size = 4
print s.format
print s.size

class Struct:
	def __init__(self, format):
		self.format = format
		self.size = struct.calcsize(format)
	def pack(self, *args):
		return struct.pack(self.format, *args)
	def unpack(self, *args):
		return struct.unpack(self.format, *args)

s = Struct('i')
print s.format
print s.size

class Struct:
	def __init__(self, format):
		self.format = format
		self.size = struct.calcsize(format)
	def pack(self, *args):
		return struct.pack(self.format, *args)
	def unpack(self, *args):
		return struct.unpack(self.format, *args)
	def unpack_from(self, *args):
		return struct.unpack_from(self.format, *args)
