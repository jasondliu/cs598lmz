from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, type(FunctionType)))

b = [x for x in [1]]
print(type(b))
print(isinstance(b, GeneratorType))
print(isinstance(b, FunctionType))
print(isinstance(b, type(FunctionType)))

c = [x for x in [1] if x > 0]
print(type(c))
print(isinstance(c, GeneratorType))
print(isinstance(c, FunctionType))
print(isinstance(c, type(FunctionType)))

d = [x for x in [1] if x > 0 else 0]
print(type(d))
print(isinstance(d, GeneratorType))
print(isinstance(d, FunctionType))
print(isinstance(d, type(FunctionType)))

e = (x for x in [1] if x > 0)
print(type(e))
print(isinstance(e, GeneratorType))
print(is
