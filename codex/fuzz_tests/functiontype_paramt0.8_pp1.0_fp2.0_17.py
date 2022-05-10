from types import FunctionType
list(FunctionType('a', FunctionType.__globals__, 'b', ('c',), ('d',)))

# the function type should display itself as the function name and a pointer to its code
FunctionType.__name__

# validate resetting the name for a function type
FunctionType.__name__ = 'foo'
FunctionType.__name__
FunctionType.__name__ = '__name__'
FunctionType.__name__

# add these to globals so cleanup can occur
globals()['FunctionType'] = FunctionType
globals()['f'] = f
