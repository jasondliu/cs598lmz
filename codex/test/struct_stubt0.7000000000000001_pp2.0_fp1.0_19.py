from _struct import Struct
s = Struct.__new__(Struct)
s.size = 10
s.format = '<L'
s.unpack(b'\10')

# In [40]: from _struct import Struct
#    ...: s = Struct.__new__(Struct)
#    ...: s.size = 5
#    ...: s.format = 'L'
#    ...: s.unpack(b'\10')
# ---------------------------------------------------------------------------
# error                                     Traceback (most recent call last)
# <ipython-input-40-ebd2c7c1bbc8> in <module>()
#       2 s = Struct.__new__(Struct)
#       3 s.size = 5
# ----> 4 s.format = 'L'
#       5 s.unpack(b'\10')
#
# _struct.pyx in _struct.Struct._set_format()
#
# TypeError: unpack requires a string argument of length 4

# In [41]: from _struct import Struct
#    ...: s = Struct.__new__(Struct)
#    ...: s.size = 5

