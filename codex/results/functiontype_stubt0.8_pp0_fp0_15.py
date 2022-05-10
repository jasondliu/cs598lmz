from types import FunctionType
a = (x for x in [1])
print(a)
print(isinstance(a, Iterator))

print(isinstance(abs, FunctionType))
