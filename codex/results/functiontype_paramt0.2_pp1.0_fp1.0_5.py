from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# FunctionType(code, globals, name, defaults, closure)
# code: the compiled function body
# globals: the global namespace in which the function should be executed
# name: the function name
# defaults: the default values of the arguments
# closure: the variables from the outer scope that the function should close over

# FunctionType.__code__
# FunctionType.__defaults__
# FunctionType.__globals__
# FunctionType.__closure__

# FunctionType.__name__
# FunctionType.__qualname__

# FunctionType.__annotations__
# FunctionType.__kwdefaults__

# FunctionType.__dict__
# FunctionType.__doc__
# FunctionType.__module__
# FunctionType.__text_signature__
# FunctionType.__closure__

# FunctionType.__globals__
# FunctionType.__code__
# FunctionType.__defaults__
# FunctionType.__kwdefaults__
# FunctionType.__dict__
# FunctionType.__
