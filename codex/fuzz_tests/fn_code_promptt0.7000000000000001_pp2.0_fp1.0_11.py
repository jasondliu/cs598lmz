fn = lambda: None
# Test fn.__code__.co_freevars, fn.__closure__, fn.__code__.co_cellvars
try:
    fn.__code__.co_freevars
except AttributeError:
    pass
else:
    raise AssertionError
try:
    fn.__closure__
except AttributeError:
    pass
else:
    raise AssertionError
try:
    fn.__code__.co_cellvars
except AttributeError:
    pass
else:
    raise AssertionError
# Test fn.__code__.co_varnames
try:
    fn.__code__.co_varnames
except AttributeError:
    pass
else:
    raise AssertionError
# Test fn.__code__.co_stacksize
try:
    fn.__code__.co_stacksize
except AttributeError:
    pass
else:
    raise AssertionError
# Test fn.__code__.co_flags
try:
    fn.__code__.co_flags
except AttributeError:
   
