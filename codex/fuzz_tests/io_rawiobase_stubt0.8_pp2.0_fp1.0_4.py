import io
class File(io.RawIOBase):
	def __init__(self, filename, mode='w'):
		self = self.__new__(File, filename, mode)
		self._Filename = filename
		self._Mode = mode
		self._Size = 0
		self._File = None
		self._Open()
	
	def __new__(cls, filename, mode='w'):
		self = io.RawIOBase.__new__(cls)
		return self
	
	def __repr__(self):
		return "File('{0}', '{1}')".format(self._Filename, self._Mode)
	
	def _Open(self):
		if self._File is not None:
			return
		
		if '+' in self._Mode:
			self._File = open(self._Filename, self._Mode, -1)
		else:
			self._File = open(self._Filename, self._Mode)
		
		if 'b' not in self._Mode:
	
