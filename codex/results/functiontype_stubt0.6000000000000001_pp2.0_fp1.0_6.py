from types import FunctionType
a = (x for x in [1])
b = [x for x in [1]]
print(isinstance(a, GeneratorType), isinstance(b, GeneratorType), isinstance(lambda x: x, FunctionType))
