fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #24071: __code__ should be writable on built-in functions
def f(): pass
f.__code__ = None

# Issue #24071: __code__ should be writable on built-in methods
class C:
    def m(self): pass
C.m.__code__ = None

# Issue #24071: __code__ should be writable on built-in class methods
class C:
    @classmethod
    def cm(cls): pass
C.cm.__code__ = None

# Issue #24071: __code__ should be writable on built-in static methods
class C:
    @staticmethod
    def sm(): pass
C.sm.__code__ = None

# Issue #24071: __code__ should be writable on built-in functions
def f(): pass
f.__code__ = None

# Issue #24071: __code__ should be writable on built-in functions
def f(): pass
f.__code__ = None

# Issue #24071
