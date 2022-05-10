fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# TypeError: 'generator' object is not callable

# https://bugs.python.org/issue31050
# https://bugs.python.org/issue31050#msg303970

# The bug is in the code object's __call__ method, which unconditionally
# calls PyCode_New, which expects a code object.

# The fix is to check for a generator object and call its __next__ method.

# The fix is in Python 3.7.
