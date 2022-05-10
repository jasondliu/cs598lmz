gi = (i for i in ())
# Test gi.gi_code
gi.gi_code
# Support for sys._getframe
try:
    import sys
    sys._getframe(0)
except (AttributeError, ValueError):
    raise ImportError(
        "This version of Python doesn't support sys._getframe(0)")


# This is silly, but with Python 2.4, when using 2to3, if you
# import foo.types, it will also try to import foo.types3.
# With Python 2.6, this will only import foo.types once.
# Python 2.6 makes it so that the module doesn't get doubly
# imported.
try:
    import types as types_26
except ImportError:
    pass
try:
    import types
except ImportError:
    import types3 as types
assert types is types_26


# Make sure that we can use __doc__
def some_func():
    """This is the docstring"""
    pass
assert some_func.__doc__ == "This is the docstring"

# Check that we can use try/except/finally
try:
    raise ValueError
