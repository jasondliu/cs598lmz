fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #14073: Test that the __code__ attribute of a builtin function
# cannot be set to a non-code object.
fn = lambda: None
fn.__code__ = None
try:
    fn.__code__ = 1
except TypeError:
    pass
else:
    print("should have raised TypeError")

# Issue #14073: Test that the __code__ attribute of a builtin function
# cannot be set to a code object with a different number of arguments.
fn = lambda: None
fn.__code__ = (lambda x: None).__code__
try:
    fn.__code__ = (lambda x, y: None).__code__
except ValueError:
    pass
else:
    print("should have raised ValueError")

# Issue #14073: Test that the __code__ attribute of a builtin function
# cannot be set to a code object with a different number of keyword-only
# arguments.
fn = lambda: None
fn.__code__ = (lambda x: None).__code__
try:

