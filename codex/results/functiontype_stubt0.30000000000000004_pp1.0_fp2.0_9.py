from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a is b)
print(type(a))
print(type(b))
print(type(a) is type(b))

print(type(a) == type(b))
print(isinstance(a, type(b)))
print(isinstance(b, type(a)))

print(type(a) == FunctionType)
print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))

print(type(a) == type(FunctionType))
print(isinstance(a, type(FunctionType)))
print(isinstance(b, type(FunctionType)))

print(type(a) == type(type(FunctionType)))
print(isinstance(a, type(type(FunctionType))))
print(isinstance(b, type(type(FunctionType))))

print(type(a) == type(type(type(FunctionType))))
print(isinstance(a, type(type(type(FunctionType)))))
print(isinstance(b, type(type(type(FunctionType)))))
