fn = lambda: None
# Test fn.__code__.co_varnames
setattr(fn, '__code__', type('code', (object,), {'co_varnames': ('a',)}))

# Test fn.__code__.co_cellvars
setattr(fn, '__code__', type('code', (object,), {'co_cellvars': ('b',)}))

# Test fn.__code__.co_freevars
setattr(fn, '__code__', type('code', (object,), {'co_freevars': ('c',)}))


# Test fn.__code__.co_varnames
def fn():
    """Function with a docstring."""
    pass


# Test fn.__code__.co_cellvars
def fn():
    """Function with a docstring."""
    a = 1


# Test fn.__code__.co_freevars
def fn():
    """Function with a docstring."""
    a = 1
    b = 2
    c = 3
