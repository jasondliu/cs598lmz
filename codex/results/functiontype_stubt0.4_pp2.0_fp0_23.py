from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))
print(type(a.__next__()))

print(type(lambda x: x))
print(type(FunctionType))
print(type(FunctionType(lambda x: x, {})))

print(type(FunctionType(lambda x: x, {})) == type(lambda x: x))
print(type(FunctionType(lambda x: x, {})) == FunctionType)

print(type(FunctionType(lambda x: x, {})) == type(FunctionType))
print(type(FunctionType(lambda x: x, {})) == type(type))
print(type(type) == type(type))

print(type(type(FunctionType(lambda x: x, {}))))
print(type(type(FunctionType(lambda x: x, {}))) == type)
print(type(type(FunctionType(lambda x: x, {}))) == type(type))

print(type(type(FunctionType(lambda x: x, {}))) == type(type(FunctionType(lambda x: x, {}))))

