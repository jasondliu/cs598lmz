import io
class File(io.RawIOBase):
	"""File(fd, mode='rb', closefd=True) -> file object

	Open a file given a file descriptor.  If the file descriptor is
	invalid, an io.UnsupportedOperation will be raised.  If closefd is
	False, the underlying file descriptor will be kept open when the file
	is closed.  The mode can be 'r', 'w', 'x', 'a', or 'b'.  The file
	allows reading, writing and seeking.
	"""
	def __new__(self, fd, mode="rb", closefd=True):
		"""Create an instance of the File type"""
		return os.fdopen(fd, mode, closefd)
		return fd.__class__.__new__(self, fd, mode, closefd)
	def __init__(self, *args, **kwargs): pass
	def detach(self, *args, **kwargs): pass
	def fileno(self, *args, **kwargs): pass
	def isatty(self, *args, **kwargs): pass
	def readable(self
