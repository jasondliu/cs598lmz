fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #24091: __code__ is not writable on built-in functions
def f(): pass
try:
    f.__code__ = None
except TypeError:
    pass
else:
    print("TypeError not raised")

# Issue #24091: __code__ is not writable on built-in methods
class C:
    def m(self): pass
try:
    C.m.__code__ = None
except TypeError:
    pass
else:
    print("TypeError not raised")

# Issue #24091: __code__ is not writable on built-in methods
class C:
    def m(self): pass
try:
    C().m.__code__ = None
except TypeError:
    pass
else:
    print("TypeError not raised")

# Issue #24091: __code__ is not writable on built-in methods
class C:
    def m(self): pass
try:
    C.__dict__['m'].__code__ = None
except TypeError:

