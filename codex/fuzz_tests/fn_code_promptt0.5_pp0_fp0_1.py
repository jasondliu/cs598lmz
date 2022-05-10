fn = lambda: None
# Test fn.__code__.co_argcount
# Test fn.__code__.co_firstlineno
# Test fn.__code__.co_flags
# Test fn.__code__.co_lnotab
# Test fn.__code__.co_name
# Test fn.__code__.co_names
# Test fn.__code__.co_nlocals
# Test fn.__code__.co_stacksize
# Test fn.__code__.co_varnames

# Test fn.__code__.co_consts
# Test fn.__code__.co_freevars
# Test fn.__code__.co_cellvars

# Test fn.__code__.co_filename
# Test fn.__code__.co_name

def test_fn():
    x = 1
    def in_fn():
        return x
    return in_fn

fn = test_fn()

# Test fn.__code__.co_argcount
# Test fn.__code__.co_firstlineno
# Test fn.__code__.co_flags
