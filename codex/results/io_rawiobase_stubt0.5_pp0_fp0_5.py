import io
class File(io.RawIOBase):
	"""
	A file-like object that wraps a :class:`~io.RawIOBase` object and adds
	support for file locking.
	
	:param f: The file-like object to wrap.
	:param lock_type: The type of lock to use.
	"""
	def __init__(self, f: io.RawIOBase, lock_type: int = LOCK_SH):
		self.__f = f
		self.__lock_type = lock_type
		self.__lock = None
	
	def __getattr__(self, name: str):
		return getattr(self.__f, name)
	
	def acquire(self, blocking: bool = True) -> bool:
		"""
		Acquire the lock.
		"""
		if self.__lock is not None:
			# Already locked
			return True
		
		try:
			self.__lock = Lock(self.__f, self.__lock_type, LOCK_NB if not blocking else 0
