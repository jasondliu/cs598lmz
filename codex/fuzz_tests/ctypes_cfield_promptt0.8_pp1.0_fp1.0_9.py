import ctypes
# Test ctypes.CField for struct _fields_ attribute
class C(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int)]

class D(C):
    _fields_ = [('b', ctypes.c_int)]

print C._fields_
print D._fields_

C._fields_ = []
x = C()

class E(ctypes.Structure):
    pass

print E._fields_

# testing fields()
ctypes.c_int
print ctypes.c_int.fields()

print ctypes.c_short.fields()

class F(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int)]

print F.fields()

class G(F):
    _fields_ = [('b', ctypes.c_int)]

print G.fields()

F.a
print F.a.fields()
