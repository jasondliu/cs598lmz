fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #23984: __code__ should not be writable on built-in functions
def f(): pass
def g(): pass
f.__code__ = g.__code__

# Issue #23984: __code__ should not be writable on built-in methods
class C:
    def m(self): pass
C.m.__code__ = C.__init__.__code__

# Issue #23984: __code__ should not be writable on built-in methods
class C:
    def m(self): pass
C().m.__code__ = C.__init__.__code__

# Issue #23984: __code__ should not be writable on built-in methods
class C:
    def m(self): pass
C.m.__code__ = C().__init__.__code__

# Issue #23984: __code__ should not be writable on built-in methods
class C:
    def m(self): pass
C().m.__code__ = C().__init__.__
