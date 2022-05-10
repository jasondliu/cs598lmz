import io
class File(io.RawIOBase):
	"""An abstract, file-like object.
	File objects are implemented using two internal buffers and a Posix file
	descriptor.  One of the internal buffers is used for input and the other
	for output.  After a seek(0), due to a read or write, the next operation
	is on the opposite buffer.  This is because Posix read and write
	operations on a file descriptor cannot be mixed; also, seek()ing
	forward, then back, loses buffered data.  Hence the need for the
	separate input and output buffers.
	"""

	# This is a cache of open files.  It maps from cache keys to file
	# objects.
	_cache = {}
	# _fmode is the mode to open files with.  It can be overridden in a
	# subclass.
	_fmode = 'w+'
	# _fd is the actual file description.  It can be overridden in a
	# subclass.
	_fd = None
	# _closed is True if the file is closed.
	_closed = False

	def __init__(self,
