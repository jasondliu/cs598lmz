import io
class File(io.RawIOBase):
	def __init__(self,path,mode='r',**kwargs):
		self.path=path
		self.mode=mode
		self.kwargs=kwargs
		self._f=None
	def read(self,size=-1):
		if self._f is None:
			self._f=open(self.path,'rb')
		if size<0:
			return self._f.read()
		else:
			return self._f.read(size)
	def write(self,b):
		if self._f is None:
			self._f=open(self.path,'wb')
		return self._f.write(b)
	def close(self):
		if self._f is not None:
			self._f.close()
			self._f=None
	def __del__(self):
		self.close()
	def __enter__(self):
		return self
	def __exit__(self,exc_type,exc_
