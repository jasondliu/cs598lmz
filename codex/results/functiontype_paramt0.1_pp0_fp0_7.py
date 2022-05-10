from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# TypeError: 'function' object is not iterable
list(FunctionType(lambda x: x, globals(), 'function'))

# TypeError: 'type' object is not iterable
list(FunctionType(lambda x: x, globals(), 'type'))

# TypeError: 'classobj' object is not iterable
list(FunctionType(lambda x: x, globals(), 'classobj'))

# TypeError: 'instance' object is not iterable
list(FunctionType(lambda x: x, globals(), 'instance'))

# TypeError: 'method-wrapper' object is not iterable
list(FunctionType(lambda x: x, globals(), 'method-wrapper'))

# TypeError: 'builtin_function_or_method' object is not iterable
list(FunctionType(lambda x: x, globals(), 'builtin_function_or_method'))

# TypeError: 'instancemethod' object is not iterable
list(FunctionType(lambda x: x, globals(), 'instance
