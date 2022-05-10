fn = lambda: None
# Test fn.__code__.co_paramcount regardless of python version
if getattr(fn.__code__, 'co_kwonlyargcount', None):  # Python 3
    param_count = fn.__code__.co_argcount - fn.__code__.co_kwonlyargcount
else:  # Python 2
    param_count = fn.__code__.co_argcount

assert param_count == 1
