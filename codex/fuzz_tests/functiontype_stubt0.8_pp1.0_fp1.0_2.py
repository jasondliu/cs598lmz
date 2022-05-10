from types import FunctionType
a = (x for x in [1])
b = (y for y in [1,2])
print a


print(type(a))
print(type(b))

print(FunctionType)

c = repr(a)
print c
print type(c)
d = str(b)
print d
