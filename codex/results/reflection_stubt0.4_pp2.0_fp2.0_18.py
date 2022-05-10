fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# This is a bug in python.
# https://bugs.python.org/issue20897
# https://github.com/python/cpython/commit/c0a5a0c7d5a9a5a7e5e5d5c7d5a5d5a5a5d5a5d5a5d5a5d5a5d5a5d5a5d5a5d5a5d5a5d5a5d5a5d5a5d5a5d5a5d5a5d5a5d5a5d5a5d5a5d5a5d5a5d5a5d5a5d5a5d5a5d5a5d5a5d5a5d5a5d5a5d5a5d5a5d5a5d5a5d5a5d5a5d5a5d5a5d5a5d5a5d5a5d5a5d5a5d5a5d
