fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #24071: __code__ of a built-in function should be read-only
def f(): pass
f.__code__ = None

# Issue #24071: __code__ of a built-in method should be read-only
class C:
    def f(self): pass
C().f.__code__ = None

# Issue #24071: __code__ of a built-in method should be read-only
class C:
    def f(self): pass
C.f.__code__ = None

# Issue #24071: __code__ of a built-in method should be read-only
class C:
    def f(self): pass
C.__dict__['f'].__code__ = None

# Issue #24071: __code__ of a built-in method should be read-only
class C:
    def f(self): pass
C.__dict__['__dict__']['f'].__code__ = None

# Issue #24071: __code__ of a built-in method
