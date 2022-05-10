gi = (i for i in ())
# Test gi.gi_code is now None

def f():
    pass

assert f.__code__.co_freevars == f.__closure__ is None
assert f.__closure__ is None

def f(x):
    def g():
        return x
    return g

assert f(42).__code__.co_freevars == ('x',)
assert f(42).__closure__ == (mockup(42),)

def make_adder(x):
    def add(y):
        return x + y
    return add

assert make_adder(5).__code__.co_freevars == ('x',)
assert make_adder(5).__closure__ == (mockup(5),)
assert make_adder(5)(10) == 15

# Test that object.__new__(type) returns uninitialized instance

class A(object):
    def __init__(self):
        self.x = 5

a = A.__new__(A)
assert not hasattr(a, 'x')

# Issue 548: objects that implement
