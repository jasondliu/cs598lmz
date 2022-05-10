from _struct import Struct
s = Struct.__new__(Struct)
s.format = Struct("<i")
s.o = s.format.obj
s.i = s.format.i
s.pack = s.format.pack
s.unpack = s.format.unpack
s.size = s.format.size
s.error = IndexError

try:
	from _struct import __doc__
except ImportError:
	__doc__ = 'a module to convert between Python values and C structs'

# Stateless, type-specific struct packing/unpacking routines
#
# Struct objects (as created by Struct()) are stateless: one
# can pack multiple times using the same object.
#

def calcsize(fmt):
	"""calcsize(format) -> integer

	Return size in bytes of the struct described by the format string.
	"""
	s = Struct(fmt).format
