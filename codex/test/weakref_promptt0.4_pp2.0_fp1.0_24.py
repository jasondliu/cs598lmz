import weakref
# Test weakref.ref() on a function.
def f():
    pass
ref = weakref.ref(f)
assert ref() is f
assert ref() is f
assert ref() is f
assert ref() is f

# Test weakref.ref() on a builtin function.
ref = weakref.ref(len)
assert ref() is len
assert ref() is len
assert ref() is len
assert ref() is len

# Test weakref.ref() on a method.
class C:
    def m(self):
        pass
c = C()
ref = weakref.ref(c.m)
assert ref() is c.m
assert ref() is c.m
assert ref() is c.m
assert ref() is c.m

# Test weakref.ref() on a builtin method.
ref = weakref.ref(c.__repr__)
assert ref() is c.__repr__
assert ref() is c.__repr__
assert ref() is c.__repr__
assert ref() is c.__repr__

# Test weakref.ref() on
