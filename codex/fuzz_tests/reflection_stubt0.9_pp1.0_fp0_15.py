fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
assert hash(gi.gi_code) == hash(fn.__code__)
assert weakref.ref(gi.gi_code)() is fn.__code__

"""
class A:
    def __init__(self, x):
        self.x = x
mi = methodcaller('x')
a = A(mi)
with pytest.raises(TypeError) as excinfo:
    hash(mi)
assert 'unhashable' in str(excinfo.value)
with pytest.raises(TypeError) as excinfo:
    hash(a.x)
assert 'unhashable' in str(excinfo.value)
"""

def S(x):
    yield x + 1
    yield x + 2
    yield x + 3

def gen():
    yield 99
    return 100

def X(*args):
    yield args

# Test that __code__ has a reference cycle through itself
c = X().__code__
assert weakref.getweakrefcount(c) == 2
r = weakref.ref(
