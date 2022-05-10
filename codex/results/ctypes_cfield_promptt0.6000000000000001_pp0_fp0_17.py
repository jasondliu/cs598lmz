import ctypes
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [('a', ctypes.c_double),
                ('b', ctypes.c_double)]

class D(ctypes.Structure):
    _fields_ = [('a', ctypes.c_char),
                ('b', C)]

class E(ctypes.Structure):
    _fields_ = [('a', ctypes.c_char),
                ('b', ctypes.CField(C))]

print D().b.a
print E().b.a

# Test ctypes.CField with _fields_

class F(ctypes.Structure):
    _fields_ = ctypes.CField(C)

print F().a

# Test ctypes.CField with _pack_

class G(ctypes.Structure):
    _pack_ = 2
    _fields_ = [('a', ctypes.CField(C))]

print G()
