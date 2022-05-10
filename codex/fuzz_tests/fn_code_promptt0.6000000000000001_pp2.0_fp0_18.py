fn = lambda: None
# Test fn.__code__.co_filename
def fn():
    pass
# Test fn.__code__.co_firstlineno
def fn():
    pass
# Test fn.__code__.co_flags
def fn():
    pass
# Test fn.__code__.co_freevars
def fn():
    pass
# Test fn.__code__.co_lnotab
def fn():
    pass
# Test fn.__code__.co_name
def fn():
    pass
# Test fn.__code__.co_names
def fn():
    pass
# Test fn.__code__.co_nlocals
def fn():
    pass
# Test fn.__code__.co_stacksize
def fn():
    pass
# Test fn.__code__.co_varnames
def fn():
    pass
# Test fn.__code__.replace()
def fn(x):
    return x + 1

def fn2(x):
    return any((x,))

fn.__code__ = fn.__code__.replace(co_code=fn2
