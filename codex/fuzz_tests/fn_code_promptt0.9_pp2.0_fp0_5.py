fn = lambda: None
# Test fn.__code__ is not working with pyinstaller
# because the declared attr is absent
if hasattr(fn, "__code__"):
    ci  = fn.__code__
    assert ci.co_argcount == 0
    assert ci.co_flags == 67 and isinstance(ci.co_varnames, tuple)

fn.__code__ = None

del fn

class d(dict):
    def __init__(self):
        self.abc = 'abc'
        self.z = 100

class S:
    def method(self, a):
        self.a = a

def method(self, a):
    self.a = a

assert S().a == S.method(S(), 1).a == method(S(), 1).a == 1

def m(a):
    return a + 1

assert S().a == S.method(S(), 1).a == method(S(), 1).a == 1

o = S()
S().a == method(S(), 1).a
del o

o = []
o[:]

