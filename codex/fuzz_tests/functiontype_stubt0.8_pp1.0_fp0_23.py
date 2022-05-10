from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(a is b)
print(hash(a) == hash(b))

print(isinstance(sum, FunctionType))
print(isinstance(lambda x: 1, FunctionType))

print(a.__next__())
print(a.__next__())
# print(a.__next__())
# print(a.__next__())
