import ctypes
# Test ctypes.CFUNCTYPE
def set_proc_name(name):
	if not isinstance(name, bytes):
		raise TypeError
	libc = ctypes.CDLL("libc.so.6", use_errno=True)
	libc.prctl(15, name, 0, 0, 0)

