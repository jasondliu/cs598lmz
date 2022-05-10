from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))

b = (x for x in [1])
print(b)
print(type(b))

print(a == b)
print(a.__next__())
print(b.__next__())
print(a.__next__())

a = (x for x in [1, 2, 3])
print(a)
for i in a:
    print(i)

a = (x for x in [1, 2, 3])
print(a)
for i in a:
    print(i)

a = (x for x in [1, 2, 3])
b = (x for x in [1, 2, 3])
print(a == b)
print(a.__next__())
print(b.__next__())

a = (x for x in [1, 2, 3])
b = (x for x in [1, 2, 3])
print(a == b)
print(a.__next__())
print(b.__next__())

a = (x
