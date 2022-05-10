fn = lambda: None
# Test fn.__code__
# Test fn.__code__.co_argcount
try:
    fn.__code__.co_argcount = 1
except AttributeError:
    pass
else:
    raise Exception("__code__.co_argcount must be read-only")
# Test fn.__code__.co_nlocals
try:
    fn.__code__.co_nlocals = 1
except AttributeError:
    pass
else:
    raise Exception("__code__.co_nlocals must be read-only")
# Test fn.__code__.co_varnames
try:
    fn.__code__.co_varnames = 1
except AttributeError:
    pass
else:
    raise Exception("__code__.co_varnames must be read-only")
# Test fn.__code__.co_filename
try:
    fn.__code__.co_filename = "test"
except AttributeError:
    pass
else:
    raise Exception("__code__.co_filename must be read-only")
# Test fn.__
