import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CFieldPtr = type(ctypes.pointer(S.x))

class C(ctypes.Structure):
    _fields_ = [('ptr', ctypes.CFieldPtr)]

# exercise ctypes.CField and ctypes._pointer_type_cache
v = C()
print v.ptr, type(v.ptr)
v.ptr = v.ptr
print v.ptr, type(v.ptr)

# verify that setting a CFiledPtr to a wrong type raises TypeError
try:
    v.ptr = 42
except TypeError:
    pass
else:
    print "this should have raised"
print

# test that only the actual type is checked, but not the base class
class D(S):
    pass

v = C()
v.ptr = D.x
print D.x
print type(D.x)
print v.ptr, type(v.ptr)

# test that setting a CFiledPtr to a value of its actual type is OK
v.ptr = S.x
print v.ptr
print type(v.ptr
