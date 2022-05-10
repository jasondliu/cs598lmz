import ctypes
# Test ctypes.CField's __hash__().
class Foo(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int)]


for p in Foo._fields_:
    print(hash(p))

print(sorted(list(set(Foo._fields_))))
