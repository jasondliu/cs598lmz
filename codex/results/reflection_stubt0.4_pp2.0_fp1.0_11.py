fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'code' object is not callable

# This is a bug in CPython, but it's not a bug in the Python language.
# The language doesn't specify that code objects are callable,
# and the documentation for the code type doesn't say anything about it either.
# The documentation for the function type says that functions have a __code__ attribute,
# but it doesn't say anything about what type that attribute should have.
# The documentation for the builtin function type says that it has a __code__ attribute,
# and that it's a code object, but it doesn't say anything about what type code objects should be.
# The documentation for the code type says that it has a co_code attribute,
# but it doesn't say anything about what type that attribute should have.
# The documentation for the builtin code type says that it has a co_code attribute,
# and that it's a string, but it doesn't say anything about what type strings should be.
