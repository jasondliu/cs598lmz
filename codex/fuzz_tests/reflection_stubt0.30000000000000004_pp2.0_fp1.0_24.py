fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #23984: __code__ is writable on built-in functions
def f(): pass
f.__code__ = None

# Issue #23984: __code__ is writable on built-in methods
class C:
    def m(self): pass
C.m.__code__ = None

# Issue #23984: __code__ is writable on built-in methods
class D(C):
    pass
D.m.__code__ = None

# Issue #23984: __code__ is writable on built-in methods
class E(C):
    def m(self): pass
E.m.__code__ = None

# Issue #23984: __code__ is writable on built-in methods
class F(C):
    def m(self): pass
del F.m
F.m.__code__ = None

# Issue #23984: __code__ is writable on built-in methods
class G(C):
    def m(self): pass
G.m = None
G.
