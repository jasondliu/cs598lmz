fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #23897: __code__ should not be writable on built-in functions
def f(): pass
try:
    f.__code__ = None
except TypeError:
    pass
else:
    print("f.__code__ = None should have raised TypeError")

# Issue #23897: __code__ should not be writable on built-in methods
class C:
    def m(self): pass
try:
    C.m.__code__ = None
except TypeError:
    pass
else:
    print("C.m.__code__ = None should have raised TypeError")

# Issue #23897: __code__ should not be writable on built-in methods
class C:
    def m(self): pass
try:
    C().m.__code__ = None
except TypeError:
    pass
else:
    print("C().m.__code__ = None should have raised TypeError")

# Issue #23897: __code__ should not be writable on built-in methods
class C:

