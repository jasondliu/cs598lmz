from types import FunctionType
list(FunctionType(lambda: None, globals(), 'lambda'))

# TypeError: 'function' object is not iterable
list(FunctionType(lambda: None, globals(), 'function'))

# TypeError: 'function' object is not iterable
list(FunctionType(lambda: None, globals(), 'type'))

# TypeError: 'function' object is not iterable
list(FunctionType(lambda: None, globals(), 'dict'))

# TypeError: 'function' object is not iterable
list(FunctionType(lambda: None, globals(), 'list'))

# TypeError: 'function' object is not iterable
list(FunctionType(lambda: None, globals(), 'tuple'))

# TypeError: 'function' object is not iterable
list(FunctionType(lambda: None, globals(), 'set'))

# TypeError: 'function' object is not iterable
list(FunctionType(lambda: None, globals(), 'frozenset'))

# TypeError: 'function' object is not iterable
list(FunctionType(lambda: None
