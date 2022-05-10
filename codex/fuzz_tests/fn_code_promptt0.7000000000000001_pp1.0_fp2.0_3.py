fn = lambda: None
# Test fn.__code__
# fn.__code__
# fn.__code__.co_argcount
# fn.__code__.co_consts
# fn.__code__.co_code
# fn.__code__.co_names
# fn.__code__.co_varnames
# fn.__code__.co_nlocals
# fn.__code__.co_stacksize
# fn.__code__.co_flags
# fn.__code__.co_lnotab
# fn.__code__.co_freevars
# fn.__code__.co_cellvars

def fn():
    pass

# Test fn.__globals__
# fn.__globals__
# fn.__globals__.get('')

# Test fn.__module__
# fn.__module__

# Test fn.__defaults__
def fn(a=1, b=2):
    pass

# fn.__defaults__

# Test fn.__closure__

def fn():
    x = 1
   
