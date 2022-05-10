import weakref
# Test weakref.ref(Foo).__call__()

class Foo(object):
    x = 1

f = Foo()
f_ref = weakref.ref(f)

# Test the behavior of function f_ref when f is still alive.
assert f_ref() is f
assert f_ref().x == 1

f.x = 2
assert f_ref().x == 2

# Delete the only reference to f, then test the behavior of f_ref.
del f
assert f_ref() is None

# Test the behavior of f_ref if f is updated with another object.
assert f_ref() is None

f = Foo()
f.x = 2
assert f_ref() is None
