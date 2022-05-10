fn = lambda: None
gi = (i for i in ())
fn.__code__ = fn.func_code = gi.gi_code = gi
del fn, gi

class C:
    def __init__(self, a, b):
        self._a = a
        self.b = b

class D(C):
    def __init__(self, a, b, c):
        C.__init__(self, a, b)
        self.c = c
    def __getitem__(self, i):
        return i

class E(object):
    def __init__(self, a, b):
        self._a = a
        self.b = b

class F(E):
    def __init__(self, a, b, c):
        E.__init__(self, a, b)
        self.c = c
    def __getitem__(self, i):
        return i

class G(C,E):
    pass

class H(C,E):
    def __getattr__(self, name):
        return 42
    def __getitem__(self, i):

