from types import FunctionType
a = (x for x in [1])
b = [1]
print(type(a))
print(type(b))
print(type(print))
print(type(FunctionType))
print(type(lambda x: x))
print(type(abs))
print(type(a) == type(b))
print(type(a) == type(print))
print(type(a) == type(FunctionType))
print(type(a) == type(lambda x: x))
print(type(a) == type(abs))

print(isinstance(a, type(b)))
print(isinstance(a, type(print)))
print(isinstance(a, type(FunctionType)))
print(isinstance(a, type(lambda x: x)))
print(isinstance(a, type(abs)))

print(isinstance(b, type(a)))
print(isinstance(b, type(print)))
print(isinstance(b, type(FunctionType)))
print(isinstance(b, type(lambda x: x)))
print(isinstance(b, type(abs)))

print(isinstance(print,
