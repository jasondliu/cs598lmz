import weakref
# Test weakref.ref() for callable objects

class C:
    def __init__(self, arg):
        self.arg = arg
    def __call__(self, arg):
        return self.arg + arg

def f(arg):
    return arg

for o in (C(1), f):
    r = weakref.ref(o)
    assert r()(2) == o(2)
    del o
    assert r()(2) == 3

# Test weakref.ref() for callable objects with a custom __call__ method

class C:
    def __call__(self, arg):
        return arg

c = C()
r = weakref.ref(c)
assert r()(2) == 2
del c
assert r()(2) == 2

# Test weakref.ref() for callable objects with a custom __call__ method
# that raises an exception

class C:
    def __call__(self, arg):
        raise RuntimeError

c = C()
r = weakref.ref(c)
