import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('f', ctypes.CField)]

print(C.f)
print(C.f.offset)
print(C.f.size)
print(C.f.type)
print(C.f.name)
print(C.f.pack)
print(C.f.bitsize)
print(C.f.bitoffset)
print(C.f.num)
print(C.f.index)
print(C.f.flags)
print(C.f.alignment)
print(C.f.get_offset())
print(C.f.get_size())
print(C.f.get_type())
print(C.f.get_name())
print(C.f.get_pack())
print(C.f.get_bitsize())
print(C.f.get_bitoffset())
print(C.f.get_num())
print(C.f.get_index())
print(C.f.get_flags())
print(C.f
