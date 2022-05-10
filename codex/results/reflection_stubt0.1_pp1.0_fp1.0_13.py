fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #27095: __code__ should be writable for built-in functions
def f(): pass
f.__code__ = None

# Issue #27095: __code__ should be writable for built-in methods
class C:
    def m(self): pass
C.m.__code__ = None

# Issue #27095: __code__ should be writable for built-in methods
class C:
    @classmethod
    def cm(cls): pass
C.cm.__code__ = None

# Issue #27095: __code__ should be writable for built-in methods
class C:
    @staticmethod
    def sm(): pass
C.sm.__code__ = None

# Issue #27095: __code__ should be writable for built-in methods
class C:
    @property
    def p(self): pass
C.p.__code__ = None

# Issue #27095: __code__ should be writable for built-in methods
class C:
    @p.set
