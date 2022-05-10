from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
# print(a.__next__())
# print(a.__next__())

print(type(a) == type(b))

a1 = FunctionType(lambda:0,{})
a2 = FunctionType(lambda:0,{})

print(a1 == a2)
print(type(a1) == type(a2))

print(type(a1))
print(type(a2))
