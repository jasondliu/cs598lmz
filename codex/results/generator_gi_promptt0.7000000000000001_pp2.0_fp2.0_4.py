gi = (i for i in ())
# Test gi.gi_code is set (it's not set for empty generators).
assert gi.gi_code is gi.send.__code__
assert len(gi.gi_frame.f_lasti.to_bytes(2, 'little', signed=True)) == 2

# Test to ensure that co_lnotab is indeed variable length.
def f(x):
    pass

assert len(f.__code__.co_lnotab) == 4

def g(x, y):
    pass

assert len(g.__code__.co_lnotab) == 8

def h(x, y, z):
    pass

assert len(h.__code__.co_lnotab) == 8

def i(x, y, z, a):
    pass

assert len(i.__code__.co_lnotab) == 12

def j(x, y, z, a, b):
    pass

assert len(j.__code__.co_lnotab) == 12

def k(x, y, z, a, b, c
