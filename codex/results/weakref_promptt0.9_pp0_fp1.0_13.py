import weakref
# Test weakref.ref for callable objects (only valid for ref objects).
def f():
    pass
r = weakref.ref(f)
print type(r)
isinstance(r(), types.BuiltinFunctionType)
print r() is f
print list(r) == [f] and list(r) == list(r) # get, dereference
del f
isinstance(r(), types.BuiltinFunctionType)
print r() is r()
print r() is None
# Test weakref.proxy for callable objects.
def g():
    pass
x = weakref.proxy(g)
print r() is f
print x is g
print x() is f()
print x() is g()
isinstance(x, types.BuiltinFunctionType)
import __builtin__
print x.__doc__ == __builtin__.g.__doc__
print x() is None
print x() is None
del g
print x.__doc__ == __builtin__.str.__doc__
print x() is None
print x() is None
# Test that non-callable objects cannot be prox
