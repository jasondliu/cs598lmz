from types import FunctionType
list(FunctionType(FunctionType.__code__, FunctionType.__globals__, 'foo', FunctionType.__defaults__, FunctionType.__closure__))

# TypeError: 'code' object is not iterable

#list(type(FunctionType))

# TypeError: 'type' object is not iterable

#list(FunctionType.__code__)

# TypeError: 'code' object is not iterable

#list(type(FunctionType.__code__))

# TypeError: 'type' object is not iterable

#list(FunctionType.__code__.__code__)

# AttributeError: 'code' object has no attribute '__code__'


#list(type(FunctionType.__code__.__code__))

# AttributeError: 'type' object has no attribute '__code__'


#list(FunctionType.__code__.__code__.__code__)

# AttributeError: 'code' object has no attribute '__code__'


#list(type(FunctionType.__code__.__code__.
