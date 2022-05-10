fn = lambda: None
# Test fn.__code__
print(fn.__code__)
print(fn.__code__.co_filename)
print(fn.__code__.co_firstlineno)
print(fn.__code__.co_varnames)

# Test fn.__closure__
print(fn.__closure__)

# Test fn.__defaults__
print(fn.__defaults__)
print(fn.__defaults__[0]())

# Test fn.__globals__
print(fn.__globals__)

# Test fn.__kwdefaults__
print(fn.__kwdefaults__)

# Test fn.__name__
print(fn.__name__)

# Test fn.__qualname__
print(fn.__qualname__)

# Test fn.__self__
print(fn.__self__)
