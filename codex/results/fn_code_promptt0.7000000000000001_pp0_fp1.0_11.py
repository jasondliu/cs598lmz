fn = lambda: None
# Test fn.__code__
setattr(fn, '__code__',
        type(fn.__code__)(fn.__code__.co_argcount, 0, 0, 0,
                          b'', b'',
                          fn.__code__.co_firstlineno,
                          b'', (), (), (),
                          fn.__code__.co_name,
                          b'', fn.__code__.co_firstlineno,
                          fn.__code__.co_lnotab))
# Test fn.__code__.co_varnames
setattr(fn.__code__, 'co_varnames', ())

# In addition to the above, check all types of functions, not just
# functions with no arguments.
def fn0(x=True): pass
def fn1(x=True): pass
def fn2(x=True, *args): pass
def fn3(x=True, **kwargs): pass
def fn4(x=True, *args, **kwargs): pass

# Ensure that the various code objects have their attributes
# correctly set.

