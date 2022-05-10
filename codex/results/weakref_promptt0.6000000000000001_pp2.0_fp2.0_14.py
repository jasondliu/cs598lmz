import weakref
# Test weakref.ref(C()) in a function.

class C: pass

def foo(x):
    r = weakref.ref(x)
    return r() is x

c = C()
assert foo(c)
assert foo(c)
assert foo(c)

# Test weakref.ref(C()) in a class.

class D:
    def __init__(self):
        self.r = weakref.ref(C())
        self.x = self.r()
    def __del__(self):
        assert self.r() is self.x

d = D()
del d

# Test weakref.ref(C()) in a class with a __del__ method.

class E:
    def __del__(self):
        assert foo(C())

e = E()
del e

# Test weakref.ref(C()) in a class with a __del__ method that calls
# weakref.ref(C()) itself.

class F:
    def __del__(self):
        assert foo(C())
        assert foo(C())
