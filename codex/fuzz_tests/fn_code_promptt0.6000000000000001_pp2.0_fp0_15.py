fn = lambda: None
# Test fn.__code__
print(fn.__code__)
# print(fn.__code__.co_filename)
# print(fn.__code__.co_name)

# Test fn.__call__
print(fn.__call__)
# print(fn.__call__.__code__.co_name)

# Test fn.__call__.__closure__
print(fn.__call__.__closure__)
# print(fn.__call__.__closure__[0].cell_contents)

# Test fn.__call__.__globals__
print(fn.__call__.__globals__)

# Test fn.__call__.__globals__['__builtins__']
print(fn.__call__.__globals__['__builtins__'])

# Test fn.__call__.__globals__['__builtins__'].__name__
print(fn.__call__.__globals__['__builtins__'].__name__)

# Test fn.__call__.__glob
