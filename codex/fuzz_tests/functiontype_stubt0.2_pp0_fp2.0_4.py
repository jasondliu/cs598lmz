from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(lambda x: x))
print(type(FunctionType))
print(type(FunctionType(lambda x: x, globals())))
print(type(FunctionType(lambda x: x, globals())()))
print(type(FunctionType(lambda x: x, globals())(1)))
print(type(FunctionType(lambda x: x, globals())(1, 2)))
print(type(FunctionType(lambda x: x, globals())(1, 2, 3)))
print(type(FunctionType(lambda x: x, globals())(1, 2, 3, 4)))
print(type(FunctionType(lambda x: x, globals())(1, 2, 3, 4, 5)))
print(type(FunctionType(lambda x: x, globals())(1, 2, 3, 4, 5, 6)))
print(type(FunctionType(lambda x: x, globals())(1, 2, 3, 4, 5, 6, 7)))
print(type(FunctionType(lambda x: x, globals())(1, 2
