fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# TypeError: 'code' object is not an iterator

# https://docs.python.org/3/reference/datamodel.html#object.__code__
# https://docs.python.org/3/library/inspect.html

# from inspect import isgeneratorfunction
# print(isgeneratorfunction(fn))

# from inspect import signature
# print(signature(fn))

# from inspect import getsource
# print(getsource(fn))
