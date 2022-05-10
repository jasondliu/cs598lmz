fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #24097: __code__ is not writable on built-in functions
def f(): pass
def g(): pass
f.__code__ = g.__code__

# Issue #24097: __code__ is not writable on built-in methods
class C:
    def f(self): pass
    def g(self): pass
C.f.__code__ = C.g.__code__

# Issue #24097: __code__ is not writable on built-in methods
class C:
    def f(self): pass
    def g(self): pass
C().f.__code__ = C().g.__code__

# Issue #24097: __code__ is not writable on built-in methods
class C:
    def f(self): pass
    def g(self): pass
C.f.__code__ = C().g.__code__

# Issue #24097: __code__ is not writable on built-in methods
class C:
    def f(self): pass
    def
