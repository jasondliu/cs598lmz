from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType), type(a))
b = [x for x in [1]]
print(isinstance(b, FunctionTy
