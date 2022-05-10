from types import FunctionType
list(FunctionType(FunctionType.__code__,'foo',FunctionType.__globals__,{},FunctionType.__closure__))

# [1, 5, 9, 13, 17]

# let's take a look at the function that was created
# this is the equivalent of a lambda
FunctionType(FunctionType.__code__,'foo',FunctionType.__globals__,{},FunctionType.__closure__)

# <function __main__.<lambda>>

# let's take a look at the code object that was used
# this is the code that was used to build the lambda
FunctionType.__code__

# <code object <lambda> at 0x103a23c30, file "<stdin>", line 1>

# let's take a look at the globals that were used
# this is the globals dictionary from the current namespace
FunctionType.__globals__

# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x1039
