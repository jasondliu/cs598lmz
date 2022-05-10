from types import FunctionType
a = (x for x in [1])
b = [x for x in [1]]
c = {x for x in [1]}
print(isinstance(a, types.GeneratorType))
print(isinstance(b, list))
print(isinstance(c, set))

f = lambda x, y : x + y
print(type(f))
print(isinstance(f, FunctionType))
