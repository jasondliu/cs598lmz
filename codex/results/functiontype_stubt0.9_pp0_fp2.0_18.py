from types import FunctionType
a = (x for x in [1])
b = a.send(2)
print(a, b)
