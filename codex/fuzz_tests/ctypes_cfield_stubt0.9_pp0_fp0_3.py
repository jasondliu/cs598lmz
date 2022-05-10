import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def foo(a, b):
    return a * b

# check that compilation really follows the typing
f = foo(2, 3)
assert (type(foo), S.x) != tuple(map(type, (foo, S.x)))

if type(foo) == ctypes.CField:
    # not on CPython
    assert False

isinstance(foo, ctypes.CField) # issue #238
isinstance(foo, ctypes.CFunction)

# we have to get out of the way now, but only after creating
# an explicit content in m to store the classes
m2 = Module().load('')

class A:
    pass

A.__name__ = 'A'

# we heard you want to raise an exception, so here it is:
class B:
    pass

# B, now please don't worry if you fail
m2.B = B
m2.B.__name__ = 'B'

m.foo = foo
m.S = S
m.A = A
m.CTY = ctypes

