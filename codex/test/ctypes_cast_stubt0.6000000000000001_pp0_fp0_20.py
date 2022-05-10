import ctypes
ctypes.cast(0, ctypes.py_object)

# Test with a weakref to a type instance
import weakref
w = weakref.ref(int)
w()

# Test with a weakref to a type instance that's gone away
class A(object): pass
w = weakref.ref(A)
del A
w()

# Test with a weakref to a type instance that's gone away
# but is still referenced by the weakref
class A(object): pass
w = weakref.ref(A)
del A
w()()

# Test with a weakref to a type instance that's gone away
# but is still referenced by the weakref
class A(object): pass
a = A()
w = weakref.ref(A)
del A
