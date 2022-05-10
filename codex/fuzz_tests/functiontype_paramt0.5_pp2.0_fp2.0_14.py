from types import FunctionType
list(FunctionType(FunctionType.__code__, globals(), "foo"))

# __code__
print(FunctionType.__code__)
print(FunctionType.__code__.co_filename)
print(FunctionType.__code__.co_name)
print(FunctionType.__code__.co_firstlineno)
print(FunctionType.__code__.co_argcount)
print(FunctionType.__code__.co_flags)
print(FunctionType.__code__.co_varnames)
print(FunctionType.__code__.co_cellvars)
print(FunctionType.__code__.co_freevars)
print(FunctionType.__code__.co_nlocals)
print(FunctionType.__code__.co_stacksize)
print(FunctionType.__code__.co_consts)
print(FunctionType.__code__.co_names)
print(FunctionType.__code__.co_varnames)

# __call__
# FunctionType.__call__(FunctionType, "foo")

# __new__

