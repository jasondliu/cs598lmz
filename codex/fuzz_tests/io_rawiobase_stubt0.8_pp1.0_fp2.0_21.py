import io
class File(io.RawIOBase):
	"""
	File descriptor wrapper for file-like objects.
	
	If the wrapped object does not have a ``readinto`` method, then
	a buffer will be allocated to achieve the same functionality.
	"""
	def __init__(self, fd):
		"""
		Create a ``File`` wrapper over the file-like object `fd`.
		"""
		if hasattr(fd, 'fileno'):
			# File descriptor wrapper
			self._fd = fd
			self._fileno = fd.fileno()
		elif hasattr(fd, 'readinto'):
			# Buffer-supporting file-like object
			self._fd = fd
			self._fileno = None
		else:
			# Standard file-like object
			self._fd = fd
			self._fileno = None
			# Allocate a buffer for readinto
			self._buffer = bytearray(io.DEFAULT_BUFFER_SIZE)
			
