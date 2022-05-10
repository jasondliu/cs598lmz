fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.__code__
fn()

class A:
    def __init__(self, i):
        self.i = i
        self.__doc__ = "a"
    def __eq__(self, other):
        return self.i == other.i
    def __lt__(self, other):
        return self.i < other.i

a = A(1)
assert a == A(1)
assert not a == A(2)
assert a < A(2)
assert a <= A(2)
assert not a < A(1)
assert a >= A(1)
assert not a > A(1)
assert not a > A(2)
assert a >= A(1)
assert a <= A(1)
assert a <= A(2)
assert a != A(2)

class B:
    def meth(self):
        "a"

assert B().meth.__doc__ == "a"

# Python 2.3
assert tuple.__new__(tuple) == ()

assert type.__new__(type
