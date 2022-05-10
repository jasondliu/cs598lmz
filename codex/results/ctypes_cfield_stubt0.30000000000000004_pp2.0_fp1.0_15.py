import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

print C.x.offset
print C.x.size
print C.x.index
print C.x.pack
print C.x.bitsize
print C.x.type
print C.x.name
print C.x.ctype
print C.x.is_base_class
print C.x.is_static
print C.x.is_volatile
print C.x.is_const
print C.x.is_bitfield
print C.x.has_virtual_dtor
print C.x.has_unnamed_bitfield
print C.x.has_trivial_ctor
print C.x.has_trivial_copy_ctor
print C.x.has_trivial_assign
print C.x.has_trivial_dtor
print C.x.has_const_ctor
print C.x.has_const_assign
print C.x.has_mutable
print C.x.
