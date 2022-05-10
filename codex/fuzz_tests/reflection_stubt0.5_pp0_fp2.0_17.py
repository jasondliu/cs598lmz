fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# Issue #31079: __code__ of a function should be a code object,
# not an arbitrary object.
def f():
    pass
fn.__code__ = 42
try:
    f.__code__ = 42
except TypeError:
    pass
else:
    print("TypeError expected")


# Issue #31138: __code__ of a function should be immutable.
def f():
    pass
try:
    f.__code__ = f.__code__
except TypeError:
    pass
else:
    print("TypeError expected")

# Issue #31138: __code__ should not be writable on classes.
class C:
    pass
try:
    C.__code__ = C.__code__
except TypeError:
    pass
else:
    print("TypeError expected")

# Issue #31138: __code__ should not be writable on modules.
try:
    sys.__code__ = sys.__code__
except TypeError:
    pass
else:
    print("TypeError expected")

# Issue #
