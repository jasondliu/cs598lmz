import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
print(isinstance(S.x, ctypes.CField))
print(isinstance(None, ctypes.CField))
print(issubclass(ctypes.c_int, ctypes.CField))
print(issubclass(int, ctypes.CField))

class Foo:
    def foo(self):
        pass
class Bar(object):
    def bar(self):
        pass
class Baz(Foo, Bar):
    pass
b = Baz()
print(issubclass(b, Baz))
print(isinstance(b, Bar))
print(A())
print(D())
print(C())

x = "adf"
print(isinstance(x, str))

def f():
    pass

class g(object):
    pass

print(issubclass(f, g))

# raises TypeError: issubclass() arg 1 must be a class
print(issubclass(g, f))
