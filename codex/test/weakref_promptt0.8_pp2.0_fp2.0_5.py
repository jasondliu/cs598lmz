import weakref
# Test weakref.ref in cpython.
# TODO: We'd like to run this test in the Pypy model for PyPy.

class Base:
    pass

class A(Base):
    pass

class B(Base):
    pass

# This class is built on the stack and does not have a __del__ method.
class Foo:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class C:
    def __del__(self):
        # Check that I can access objects of other classes.
        # This is a fragile test because it assumes that the order
        # in which __del__ gets called is deterministic.
        global y
        global yref
        assert y.a == "hello"
        assert y.b == "world"
        assert yref() is y
        y.a = "hello2"
        y.b = "world2"
        yref = weakref.ref(y)

def f0():
    a = A()
    b = B()
    w_a = weakref
