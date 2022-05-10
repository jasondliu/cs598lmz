fn = lambda: None
# Test fn.__code__

print("fn.__code__.co_filename:", fn.__code__.co_filename)
print("fn.__code__.co_firstlineno:", fn.__code__.co_firstlineno)

print("fn.__code__.co_varnames:", fn.__code__.co_varnames)
print("fn.__code__.co_argcount:", fn.__code__.co_argcount)

# Test fn.__globals__

print("fn.__globals__:", fn.__globals__)
print("fn.__globals__['__builtins__']:", fn.__globals__['__builtins__'])
print("fn.__globals__['__builtins__'].pow:", fn.__globals__['__builtins__'].pow)
print("fn.__globals__['__builtins__'].pow(2, 8):", fn.__globals__['__builtins__'].pow(2, 8
