from _struct import Struct
s = Struct.__new__(Struct)
def calcsize(fmt):
	return s.calcsize(fmt)

# Implementation of little- and big-endian int packing/unpacking
# taken from Python 2.3.3's <ctypes/c_longlong.py>
if native_str_is_unicode is True:
	bytes = lambda b, e: b.decode(e)
	maxint = int(bytes('\x7f\xff\xff\xff\xff\xff\xff\xff', 'utf-8'))
else:
	maxint = 0x7fffffffffffffffL

def to_bytes(val, _struct_I=s.pack('I', 0)):
	"""Convert an integer to a bytes object of little-endian bytes,
	without using a format string."""
	# If this is a 64-bit machine, val may be too big to
	# fit into an unsigned 32-bit, so try it with a signed 32-bit
	if abs(val) < maxint:
		_struct_I = s.pack('i', 0)

