gi = (i for i in ())
# Test gi.gi_code.co_flags
assert gi.gi_code.co_flags == 67


def f():
    pass

# Test f.__code__.co_flags
assert f.__code__.co_flags == 67

# Test f.__code__.co_lnotab
assert f.__code__.co_lnotab == b''

# Test f.__code__.co_consts
assert f.__code__.co_consts == (None,)

# Test f.__code__.co_names
assert f.__code__.co_names == tuple()

# Test f.__code__.co_varnames
assert f.__code__.co_varnames == tuple()

# Test f.__code__.co_freevars
assert f.__code__.co_freevars == tuple()

# Test f.__code__.co_cellvars
assert f.__code__.co_cellvars == tuple()

# Test f.__code__.co_filename
assert f.__code__.co
