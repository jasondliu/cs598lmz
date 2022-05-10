import io
class File(io.RawIOBase):
	def __init__(self,name,flags,*args):
		self._name=name
		self._flags=flags|os.O_BINARY
		self._file=os.open(self._name,self._flags,*args)
		self._written=False
	def fileno(self):
		return self._file
	def name(self):
		return self._name
	def isatty(self):
		return False
	def close(self):
		fl=os.fstat(self._file)
		if fl and not fl.st_size and self._written:
			os.close(self._file)
			os.unlink(self._name)
			self._file=None
			return
		return os.close(self._file)
	def seekable(self):
		return True
	def seek(self,offset,whence=os.SEEK_SET):
		return os.lseek(self._file,offset,whence)
	def tell
