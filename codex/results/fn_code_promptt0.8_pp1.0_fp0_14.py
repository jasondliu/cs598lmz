fn = lambda: None
# Test fn.__code__ is not None (i.e., not a built-in function)
if not hasattr(fn.__code__, 'co_filename'):
    raise ImportError("'fn.__code__' has no attribute 'co_filename'")
# Test fn.__code__ is not a wrapper around a built-in function
if fn.__code__.co_filename == '<string>':
    raise ImportError("fn.__code__.co_filename is '<string>'")
# (f_globals is a faster alternative to fn.func_globals.get('__file__'),
# which invokes __getitem__ when __getattr__ is undefined)
f_globals = getattr(fn, 'func_globals', None) or getattr(fn, '__globals__')
__file__ = (f_globals.get('__file__') or
            getattr(sys, '_MEIPASS', None) or
            getattr(fn.__code__, 'co_filename'))
del fn  # Get rid of fn before we load the
