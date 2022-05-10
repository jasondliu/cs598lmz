from _struct import Struct
s = Struct.__new__(Struct)
def calcsize(fmt):
	return s.calcsize(fmt)

# Implementation of little- and big-endian int packing/unpacking
# taken from Python 2.3.3's <ctypes/c_longlong.py>
if native_str_is_unicode is True:
	bytes = lambda b, e: b.decode(e)
	maxint = int(bytes('\x7f\xff\xff\xff\xff\xff\xff\xff', 'utf-8'))
