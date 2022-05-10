from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(lambda x: x))
print(type(FunctionType))
print(type(FunctionType(lambda x: x, globals())))
print(type(FunctionType(lambda x: x, globals())()))

print(type(FunctionType(lambda x: x, globals())) == FunctionType)
print(type(FunctionType(lambda x: x, globals())()) == FunctionType)

print(type(FunctionType(lambda x: x, globals())) == type(lambda x: x))
print(type(FunctionType(lambda x: x, globals())()) == type(lambda x: x))

print(type(FunctionType(lambda x: x, globals())) == type(FunctionType))
print(type(FunctionType(lambda x: x, globals())()) == type(FunctionType))

print(type(FunctionType(lambda x: x, globals())) == type(FunctionType(lambda x: x, globals())))
print(type(FunctionType(lambda x: x, globals())()) == type(Function
