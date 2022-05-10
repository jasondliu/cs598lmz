fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__code__ = None

# Issue #26167: __code__ should be read-only on built-in functions
def f():
    pass
try:
    f.__code__ = None
except TypeError:
    pass
else:
    raise Exception("__code__ should be read-only on built-in functions")

# Issue #26167: __code__ should be read-only on methods
class C:
    def m(self):
        pass
try:
    C.m.__code__ = None
except TypeError:
    pass
else:
    raise Exception("__code__ should be read-only on methods")

# Issue #26167: __code__ should be read-only on built-in methods
try:
    C.__new__.__code__ = None
except TypeError:
    pass
else:
    raise Exception("__code__ should be read-only on built-in methods")

# Issue #26167: __code__ should be read-only on built-in methods
try:
    C.__init__
