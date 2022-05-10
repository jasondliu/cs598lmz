fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# Issue #26897: segfault when __code__ is not a code object.
fn = lambda: None
fn.__code__ = 42
try:
    fn()
except TypeError:
    pass
else:
    print("Should have raised TypeError")

# Issue #26911: segfault when __code__ is a code object with NULL co_code.
fn = lambda: None
fn.__code__ = type(fn.__code__)(0, 0, 0, 0, b"", (), (), (), "", "", 0, b"")
try:
    fn()
except ValueError:
    pass
else:
    print("Should have raised ValueError")

# Issue #26915: segfault when __code__ is a code object with NULL co_consts.
fn = lambda: None
fn.__code__ = type(fn.__code__)(0, 0, 0, 0, b"", None, (), (), "", "", 0, b"")
try:
    fn()
except ValueError
