from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack(b'\x00\x00\x00\x00')

# This is a bug in Python 2.7.
# See http://bugs.python.org/issue14127
# The following should raise an error.
#s.unpack(b'\x00\x00\x00')

# This is a bug in Python 2.7.
# See http://bugs.python.org/issue14127
# The following should raise an error.
#s.unpack(b'\x00\x00\x00\x00\x00')

# This is a bug in Python 2.7.
# See http://bugs.python.org/issue14127
# The following should raise an error.
#s.unpack(b'\x00\x00\x00\x00\x00\x00')

# This is a bug in Python 2.7.
# See http://bugs.python.org/issue14127
# The following should raise an error.
#s.unpack(b'
