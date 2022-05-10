from _struct import Struct
s = Struct.__new__(Struct)
s.format = '>I'
s.size = 4
s.pack = s.pack_f
s.unpack = s.unpack_f
s.unpack_from = s.unpack_from_f
s.pack_into = s.pack_into_f
s.calcsize = s.size
s.pack(1)

class ctypes_Struct(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int)]

class ctypes_Struct_with_pack(ctypes.Structure):
    _pack_ = 2
    _fields_ = [('a', ctypes.c_int)]

class ctypes_Struct_with_pack_and_size(ctypes.Structure):
    _pack_ = 2
    _fields_ = [('a', ctypes.c_int), ('b', ctypes.c_int)]

class ctypes_Struct_with_pack_and_size_and_alignment(ctypes.Structure):
    _pack_ = 2
