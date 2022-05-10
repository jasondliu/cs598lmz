import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def f(i, j):
    return i * j

cf = FUNTYPE(f)
print f(2, 3)
print cf(2, 3)

#while True:
#    print cf(2, 3)

print cf.__doc__
print cf.__class__.__name__

print cf.__name__
print cf.__module__
print cf.__repr__()
print cf.__str__()
print cf.__nonzero__()
print cf.__bool__()
print cf.__hash__()

print cf.__dict__
print cf.__doc__
print cf.__module__
print cf.__weakref__
print cf._b_base_
print cf._objects
