import io
class File(io.RawIOBase):
	def __init__(self, *args, **kwargs):
		self.file = ctypes.c_void_p(0)
		self.opened = False
		self.rw = False
		self.size = 0
	def __del__(self):
		if self.opened:
			self.close()
	def open(self, filename, mode):
		if self.opened:
			raise IOError("File already opened")
		self.file = ctypes.c_void_p(0)
		self.size = int(ctypes.c_int32(0))
		if mode == "r":
			self.rw = False
			if not _file_open_read(filename.encode("utf-8"), ctypes.byref(self.file), ctypes.byref(self.size)):
				raise IOError("File open failed")
			self.opened = True
		elif mode == "w":
			self.rw = True
		
