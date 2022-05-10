fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #13583: test that the __code__ attribute of a built-in function
# is writable.
def f(): pass
f.__code__ = None

# Issue #13583: test that the __code__ attribute of a built-in method
# is writable.
def f(): pass
f.__code__ = None

# Issue #13583: test that the __code__ attribute of a built-in method
# is writable.
class C:
    def f(self): pass
C.f.__code__ = None

# Issue #13583: test that the __code__ attribute of a built-in method
# is writable.
class C:
    def f(self): pass
C().f.__code__ = None

# Issue #13583: test that the __code__ attribute of a built-in method
# is writable.
class C:
    @classmethod
    def f(cls): pass
C.f.__code__ = None

# Issue #13583: test that the __code__ attribute of a
