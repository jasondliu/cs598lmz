from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, Iterator))

print(isinstance(a, list))
print(isinstance(a, tuple))
print(isinstance(a, dict))
print(isinstance(a, set))

print(isinstance(a, (list, tuple, dict)))
print(isinstance(a, (list, tuple, dict, set)))
