from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# TypeError: 'module' object is not iterable
list(type(lambda x: x))

# TypeError: 'module' object is not iterable
list(type(FunctionType(lambda x: x, globals(), 'lambda')))

# TypeError: 'module' object is not iterable
list(type(type(lambda x: x)))

# TypeError: 'module' object is not iterable
list(type(type(FunctionType(lambda x: x, globals(), 'lambda'))))

# TypeError: 'module' object is not iterable
list(type(type(type(lambda x: x))))

# TypeError: 'module' object is not iterable
list(type(type(type(FunctionType(lambda x: x, globals(), 'lambda')))))

# TypeError: 'module' object is not iterable
list(type(type(type(type(lambda x: x)))))

# TypeError: 'module' object is not iterable
list(type(type(type(type(
