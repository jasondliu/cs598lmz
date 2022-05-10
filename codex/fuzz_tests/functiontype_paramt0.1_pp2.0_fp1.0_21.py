from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# TypeError: 'function' object is not iterable
# list(function)

# TypeError: 'type' object is not iterable
# list(type)

# TypeError: 'builtin_function_or_method' object is not iterable
# list(len)

# TypeError: 'module' object is not iterable
# list(sys)

# TypeError: 'getset_descriptor' object is not iterable
# list(sys.__dict__)

# TypeError: 'member_descriptor' object is not iterable
# list(sys.__doc__)

# TypeError: 'method_descriptor' object is not iterable
# list(sys.__getattribute__)

# TypeError: 'wrapper_descriptor' object is not iterable
# list(sys.__hash__)

# TypeError: 'method-wrapper' object is not iterable
# list(sys.__repr__)

# TypeError: 'method-wrapper' object is not iter
