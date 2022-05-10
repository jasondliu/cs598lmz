from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(next))
b = next(a)
print(b)

a = [1, 2, 3]
b = a
print(id(a), id(b))
b = a[:]
print(id(a), id(b))
b = a.copy()
print(id(a), id(b))

a = [1, 2, 3]
b = a
a is b

a = [1, 2, 3]
b = [1, 2, 3]
a is b

a = (1, 2, 3)
b = (1, 2, 3)
a is b

a = [1, 2, 3]
b = a
a[0] = 100
print(a, b)

a = (1, 2, 3)
b = a
a is b
a = a + (4,)
print(a, b)

a = [1, 2, 3]
b = a
a.append(4)
print(a, b)

a = (1,
