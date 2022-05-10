from types import FunctionType
a = (x for x in [1])
print(isinstance(a, Iterator))
b = [1]
print(isinstance(b, Iterator))
c = {}
print(isinstance(c, Iterator))
d = FunctionType
print(isinstance(d, Iterator))

a = [1, 2, 3]
b = a
c = a.copy()
a[0] = 100
print(b)
print(c)
print(a is b)
print(a is c)
