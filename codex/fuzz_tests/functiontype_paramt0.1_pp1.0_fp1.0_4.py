from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# TypeError: 'function' object is not iterable
list(FunctionType(lambda x: x, globals(), 'function'))

# TypeError: 'generator' object is not iterable
list(FunctionType(lambda x: x, globals(), 'generator'))

# TypeError: 'method' object is not iterable
list(FunctionType(lambda x: x, globals(), 'method'))

# TypeError: 'builtin_function_or_method' object is not iterable
list(FunctionType(lambda x: x, globals(), 'builtin_function_or_method'))

# TypeError: 'instancemethod' object is not iterable
list(FunctionType(lambda x: x, globals(), 'instancemethod'))

# TypeError: 'wrapper_descriptor' object is not iterable
list(FunctionType(lambda x: x, globals(), 'wrapper_descriptor'))

# TypeError: 'method-wrapper' object is not iterable
list(FunctionType(lambda x:
