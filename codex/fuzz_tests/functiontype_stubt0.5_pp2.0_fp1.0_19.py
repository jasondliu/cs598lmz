from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(type(a) == GeneratorType)
print(type(a) == FunctionType)
print(type(a) == type(lambda x: x))

print('='*100)

print(type(abs))
print(type(abs) == type(lambda x: x))
print(type(abs) == FunctionType)
print(type(abs) == GeneratorType)

print('='*100)

print(type(x for x in [1]))
print(type(x for x in [1]) == type(lambda x: x))
print(type(x for x in [1]) == FunctionType)
print(type(x for x in [1]) == GeneratorType)

print('='*100)

print(type(lambda x: x))
print(type(lambda x: x) == FunctionType)
print(type(lambda x: x) == GeneratorType)

print('='*100)

print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x:
