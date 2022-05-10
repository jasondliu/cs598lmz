import io
class File(io.RawIOBase):
	def write(self, b):
		pass
	def read(self, n=-1):
		return b''
	def readinto(self, b):
		pass

#	def write(self, b):
#		self._f.write(b)
#	def read(self, n=-1):
#		return self._f.read(n)
#	def readinto(self, b):
#		return self._f.readinto(b)

#	def __init__(self, f):
#		self._f = f

#	def __getattr__(self, attr):
#		return getattr(self._f, attr)

class BaseFileStorage(File):
	"""The base file storage class.

	This class provides a minimal file API, which the API of the
	:class:`~werkzeug.datastructures.FileStorage` class builds on.

	:param stream: a stream to be wrapped.  A stream is an object that
	               provides :meth:`read`,
