from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.unpack(b'\x00\x00\x00\x00')

# This is a bug in Python 3.6.0, fixed in 3.6.1
# https://bugs.python.org/issue29097
# https://github.com/python/cpython/commit/f6e8e0b9c0d8d8b8c6e1f6a0f6d8e6a9a6c5f6b2
#
# The bug is that the Struct.__init__ method does not set the
# _Struct__format attribute.
#
# The Struct.__init__ method is not called when the Struct class
# is instantiated, so the _Struct__format attribute is not set.
#
# The Struct.__new__ method does not set the _Struct__format attribute.
#
# The Struct.__init__ method is called when the Struct instance is
# instantiated, so the _Struct__format attribute is set.
#
# The Struct.__init__ method is called when the Struct instance
