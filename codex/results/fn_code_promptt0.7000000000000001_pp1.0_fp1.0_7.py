fn = lambda: None
# Test fn.__code__.co_varnames
setattr(fn, '__code__', CodeType(0, 0, 0, 0, b'', b'', (), (), (), b'', b'', 7, b'', (), (), ()) )
setattr(fn.__code__, 'co_varnames', ('x', 'y', 'z'))
del fn

# Test fn.__code__.co_argcount
def fn(x, y, z):
	pass
print(fn.__code__.co_argcount)

# Test fn.__code__.co_argcount
def fn():
	pass
print(fn.__code__.co_argcount)
