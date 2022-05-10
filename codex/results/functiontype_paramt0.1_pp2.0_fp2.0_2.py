from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# TypeError: 'function' object is not iterable
list(FunctionType(lambda x: x, globals(), 'function'))

# TypeError: 'builtin_function_or_method' object is not iterable
list(FunctionType(lambda x: x, globals(), 'builtin_function_or_method'))

# TypeError: 'method_descriptor' object is not iterable
list(FunctionType(lambda x: x, globals(), 'method_descriptor'))

# TypeError: 'wrapper_descriptor' object is not iterable
list(FunctionType(lambda x: x, globals(), 'wrapper_descriptor'))

# TypeError: 'method-wrapper' object is not iterable
list(FunctionType(lambda x: x, globals(), 'method-wrapper'))

# TypeError: 'classobj' object is not iterable
list(FunctionType(lambda x: x, globals(), 'classobj'))

# TypeError: 'instancemethod' object is not iterable
