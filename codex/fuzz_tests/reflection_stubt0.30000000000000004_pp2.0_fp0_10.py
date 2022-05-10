fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #16095: Check that the __code__ attribute of a built-in function
# is not writable.
def f(): pass
f.__code__ = 1
try:
    f.__code__ = 1
except TypeError:
    pass
else:
    raise Exception("__code__ attribute of a built-in function is writable")

# Issue #17078: Check that the __code__ attribute of a built-in method
# is not writable.
def f(): pass
f.__code__ = 1
try:
    f.__code__ = 1
except TypeError:
    pass
else:
    raise Exception("__code__ attribute of a built-in method is writable")

# Issue #17078: Check that the __code__ attribute of a method
# is not writable.
class C(object):
    def f(self): pass
c = C()
c.f.__code__ = 1
try:
    c.f.__code__ = 1
except TypeError:
    pass
else:
   
