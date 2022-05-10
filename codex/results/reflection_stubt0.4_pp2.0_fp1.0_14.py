fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #24402: Test that __code__ is not writable on built-in functions
import builtins
def test_builtin_code(name):
    try:
        builtins.__dict__[name].__code__ = None
    except TypeError:
        pass
    else:
        raise AssertionError("__code__ is writable on built-in function")

test_builtin_code('len')
test_builtin_code('abs')

# Issue #24402: Test that __code__ is not writable on built-in methods
import sys
def test_builtin_method_code(name):
    try:
        sys.__dict__[name].__code__ = None
    except TypeError:
        pass
    else:
        raise AssertionError("__code__ is writable on built-in method")

test_builtin_method_code('getrefcount')
test_builtin_method_code('getrecursionlimit')

# Issue #24402: Test that __code__ is not writable on built
