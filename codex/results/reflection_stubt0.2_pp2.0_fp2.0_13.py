fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #14096: test that the __code__ attribute of a built-in function
# is read-only.
import sys
def f(): pass
f.__code__ = None
try:
    sys.getrefcount(f.__code__)
except TypeError:
    pass
else:
    print("TypeError expected")

# Issue #14096: test that the __code__ attribute of a built-in method
# is read-only.
import sys
def f(): pass
f.__code__ = None
try:
    sys.getrefcount(int.__add__.__code__)
except TypeError:
    pass
else:
    print("TypeError expected")

# Issue #14096: test that the __code__ attribute of a built-in method
# is read-only.
import sys
def f(): pass
f.__code__ = None
try:
    sys.getrefcount(int.__add__.__code__)
except TypeError:
    pass
else:
    print("TypeError expected
