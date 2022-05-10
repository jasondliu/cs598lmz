import io
class File(io.RawIOBase):
	"""docstring for File"""
	def __init__(self):
		super(File, self).__init__()
		self.filename = ''
		self.mode = ''
		self.closed = False
		self.newlines = None
		self.softspace = 0
		self.encoding = None
		self.name = None
		self.mode = None
		self.encoding = None
		self.errors = None
		self.newlines = None
		self.__dict__['buffer'] = None
		self.__dict__['raw'] = None
		self.__dict__['line_buffering'] = False
		self.__dict__['write_through'] = False
		self.__dict__['seekable'] = True
		self.__dict__['readable'] = True
		self.__dict__['writable'] = True
		self.__dict__['closefd'] = True
	def close(self):
		self.flush()
		self._close()
