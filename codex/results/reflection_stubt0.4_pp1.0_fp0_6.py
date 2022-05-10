fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #22982: Crash when __code__ is a method that doesn't return a code
# object.
class A:
    def __code__(self):
        return None
fn.__code__ = A().__code__
fn()

# Issue #22982: Crash when __code__ is a method that returns a code object
# with a bad co_filename.
def bad_filename():
    return 42
fn.__code__ = bad_filename
fn()

# Issue #22982: Crash when __code__ is a method that returns a code object
# with a bad co_firstlineno.
def bad_firstlineno():
    return 42
fn.__code__ = bad_firstlineno
fn()

# Issue #22982: Crash when __code__ is a method that returns a code object
# with a bad co_lnotab.
def bad_lnotab():
    return 42
fn.__code__ = bad_lnotab
fn()

# Issue #22982: Crash when __code__ is a method
