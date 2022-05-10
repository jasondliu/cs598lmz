fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that the __code__ attribute is not writable.
try:
    fn.__code__ = 42
except TypeError:
    pass
else:
    print("Failed to raise TypeError")

# Test that the __code__ attribute is not deletable.
try:
    del fn.__code__
except TypeError:
    pass
else:
    print("Failed to raise TypeError")

# Test that the __code__ attribute is not inherited from a superclass.
class A:
    __code__ = 42

class B(A):
    pass

assert not hasattr(B, "__code__")

# Test that the __code__ attribute is not inherited from a superclass.
class A:
    def __init__(self):
        self.__code__ = 42

class B(A):
    pass

assert not hasattr(B(), "__code__")
