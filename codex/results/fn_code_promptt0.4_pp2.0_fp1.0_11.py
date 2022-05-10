fn = lambda: None
# Test fn.__code__.co_filename
setattr(fn, '__code__', type('', (), {'co_filename': 'filename.py'}))
# Test fn.__code__.co_firstlineno
setattr(fn, '__code__', type('', (), {'co_firstlineno': 1}))
# Test fn.__code__.co_name
setattr(fn, '__code__', type('', (), {'co_name': 'fn'}))
# Test fn.__code__.co_varnames
setattr(fn, '__code__', type('', (), {'co_varnames': ('a', 'b')}))
# Test fn.__code__.co_argcount
setattr(fn, '__code__', type('', (), {'co_argcount': 2}))
# Test fn.__code__.co_flags
setattr(fn, '__code__', type('', (), {'co_flags': 0}))
# Test fn.__code__.co_argcount
setattr(fn, '__code__', type('
