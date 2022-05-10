fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code

# __code__ is not writable
try:
    fn.__code__ = fn.__code__
except TypeError:
    pass
else:
    raise TestFailed("__code__ is writable")

# __code__ is not deletable
try:
    del fn.__code__
except TypeError:
    pass
else:
    raise TestFailed("__code__ is deletable")

# Test code objects
def f1(a):
    b = 1
    c = a + b
    return c

def f2(a):
    def g():
        return a
    b = g()
    return b

def f3(a):
    def g():
        return a
    def h():
        return g
    b = h()
    return b()

def f4(a):
    def g():
        return a
    b = g()
    def h():
        return b
    return h()

def f5(a):
    def g():
        return a
    def h():
