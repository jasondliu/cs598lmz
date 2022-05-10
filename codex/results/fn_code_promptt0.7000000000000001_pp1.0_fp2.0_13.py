fn = lambda: None
# Test fn.__code__.co_varnames
# Test fn.__code__.co_argcount
# Test fn.__code__.co_cellvars
assert fn.__code__.co_cellvars == ()
# Test fn.__code__.co_filename
assert isinstance(fn.__code__.co_filename, str)
# Test fn.__code__.co_firstlineno
assert isinstance(fn.__code__.co_firstlineno, int)
# Test fn.__code__.co_flags
assert isinstance(fn.__code__.co_flags, int)
# Test fn.__code__.co_freevars
assert fn.__code__.co_freevars == ()
# Test fn.__code__.co_kwonlyargcount
# Test fn.__code__.co_lnotab
# Test fn.__code__.co_name
assert isinstance(fn.__code__.co_name, str)
# Test fn.__code__.co_names
# Test fn.__code__.co_nlocals
# Test
