import _struct
		if len(self.__buffer) < size:
			raise RuntimeError("I/O buffer too small: %i < %i" % (len(self.__buffer), size))
		return _struct.unpack_from(self.__endian + fmt, self.__buffer, self.__offset)[0]

	def _S(self, size):
		if len(self.__buffer) < size:
			raise RuntimeError("I/O buffer too small: %i < %i" % (len(self.__buffer), size))
		value = self.__buffer[self.__offset : self.__offset + size]
		self.__offset += size
		return value

	def __str__(self):
		self.reset()
		return self.__buffer

class CStringIO(BinaryIO):
	def __init__(self, data = '', endian = '<'):
		BinaryIO.__init__(self, endian)
		self._S(data)

	def __call
