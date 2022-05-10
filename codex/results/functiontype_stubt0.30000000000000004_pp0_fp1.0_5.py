from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(lambda x: x))
print(type(FunctionType))
print(type(FunctionType(lambda x: x, globals())))

import types
print(type(types.FunctionType))

def f():
    pass

print(type(f))
print(type(f) == types.FunctionType)

def f():
    pass

print(type(f) == types.FunctionType)
print(type(f) == types.BuiltinFunctionType)
print(type(f) == types.LambdaType)
print(type(f) == types.GeneratorType)

def f():
    pass

print(type(f) == types.FunctionType)
print(type(f) == types.BuiltinFunctionType)
print(type(f) == types.LambdaType)
print(type(f) == types.GeneratorType)

def f():
    pass

print(type(f) == types.FunctionType)
print(type(f) == types.BuiltinFunctionType)

