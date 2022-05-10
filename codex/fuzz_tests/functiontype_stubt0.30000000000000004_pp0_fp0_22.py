from types import FunctionType
a = (x for x in [1])
print(type(a))

print(type(lambda x: x + 1))
print(type(abs))
print(type(FunctionType))
print(type(FunctionType(lambda x: x + 1)))

print(dir(a))
print(dir(lambda x: x + 1))
print(dir(abs))
print(dir(FunctionType))
print(dir(FunctionType(lambda x: x + 1)))

print(dir(a) == dir(lambda x: x + 1))
print(dir(abs) == dir(FunctionType))
print(dir(FunctionType(lambda x: x + 1)) == dir(FunctionType))

print(dir(a) == dir(abs))
print(dir(lambda x: x + 1) == dir(FunctionType))
print(dir(FunctionType(lambda x: x + 1)) == dir(abs))

print(dir(a) == dir(FunctionType(lambda x: x + 1)))
print(dir(lambda x: x + 1) == dir(abs))
print(dir(abs) == dir(FunctionType))
