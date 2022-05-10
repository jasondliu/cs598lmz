import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1
assert fun() == 1

# check that the cache is used
assert fun.__name__ == 'fun'
assert fun.__module__ == __name__
assert fun.__doc__ is None
assert fun.__dict__ == {}

# check that the dicts are kept
fun.__dict__['x'] = 1
assert fun.__dict__['x'] == 1
assert fun.x == 1
fun.x = 2
assert fun.x == 2
assert fun.__dict__['x'] == 2

# check that a wrapper can be created from another wrapper
def g(x):
    return x
h = FUNTYPE(g)
assert h(1) == 1
assert h.__name__ == 'g'
assert h.__dict__ == {}

# check that the type does not crash if the function has a closure
def f(x):
    y = 1
    def g(z):
        return x + y + z
    return g
g = FUNTYPE(f(1))
assert g(1) == 3

# check that the type does not
