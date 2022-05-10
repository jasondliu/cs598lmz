from _struct import Struct
s = Struct.__new__(Struct)
s.format = PY2 and 'H' or '=H'
s.size = PY2 and 2 or calcsize(s.format)

class U16BE(int):
	def __new__(cls, value):
		return super(U16BE, cls).__new__(cls, cls.validate(value))

	@staticmethod
	def validate(value):
		assert 0 <= value <= 2**16
		return value

	@staticmethod
	def unpack(stream, compressed=False):
		return U16BE(unpack(s, stream.read(s.size))[0])

	def pack(self, stream, compressed=False):
		return stream.write(pack(s, self))

	def __add__(self, other):
		return U16BE(super(U16BE, self).__add__(other))

	def __sub__(self, other):
		return U16BE(super(U16BE, self).__sub__(other))

	def __mul__(
