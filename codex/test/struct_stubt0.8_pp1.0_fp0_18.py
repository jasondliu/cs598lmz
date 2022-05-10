from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'bbccccc'
s.error = None
s.size = ctypes.sizeof(s.format)
