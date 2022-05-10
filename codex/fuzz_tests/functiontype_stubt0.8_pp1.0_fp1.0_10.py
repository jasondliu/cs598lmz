from types import FunctionType
a = (x for x in [1])
print(a)
print(isinstance(a, list))
b = [x for x in [1]]
print(b)
print(isinstance(b, list))
print(isinstance(b, GeneratorType))
print(isinstance(b, FunctionType))


print(dir(a))
print(dir(b))

# print(b.__next__())
# print(b.__next__())
