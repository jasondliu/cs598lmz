from types import FunctionType
a = (x for x in [1])
b = (x for x in range(0, 100))
a.close()
print(a.__class__)
print(b.__class__)
