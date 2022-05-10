from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo') for _ in range(10))

# Test that the __code__ attribute of a function is not a weakref.
import weakref
def f():
    pass
wr = weakref.ref(f.__code__)
del f
assert wr() is not None

# Test that the __code__ attribute of a function is not a weakref.
import weakref
def f():
    pass
wr = weakref.ref(f.__code__)
del f
assert wr() is not None

# Test that the __code__ attribute of a function is not a weakref.
import weakref
def f():
    pass
wr = weakref.ref(f.__code__)
del f
assert wr() is not None

# Test that the __code__ attribute of a function is not a weakref.
import weakref
def f():
    pass
wr = weakref.ref(f.__code__)
del f
assert wr() is not None

# Test that the __code__ attribute of a function is not a weakref.
import weak
