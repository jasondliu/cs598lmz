from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

print(dir(a))
print(a.__next__())
print(a.__next__())

# print(a.__next__())

# for i in a:
#     print(i)

# print(next(a))
# print(next(a))
