from types import FunctionType
a = (x for x in [1])
a = FunctionType(lambda x: x, globals())
print a
print a()

# FunctionType.__call__
a = FunctionType(lambda x: x, globals())
print a.__call__()
print a.__call__('hello')

# FunctionType.__repr__
a = FunctionType(lambda x: x, globals())
print a.__repr__()

# FunctionType.__str__
# FunctionType.func_name
a = FunctionType(lambda x: x, globals())
print a.__str__()
print a.func_name

# FunctionType.func_defaults
a = FunctionType(lambda x, y=1: x, globals())
print a.func_defaults

# FunctionType.func_code
a = FunctionType(lambda x, y=1: x, globals())
print a.func_code

# FunctionType.func_globals
a = FunctionType(lambda x, y=1: x, globals())
print a.func_globals

# FunctionType.
