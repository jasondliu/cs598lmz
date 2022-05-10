from types import FunctionType
a = (x for x in [1])
print(type(a))
print(a.__next__())

b = [x for x in [1]]
print(type(b))
print(b)

c = {x for x in [1]}
print(type(c))
print(c)

d = {x:x for x in [1]}
print(type(d))
print(d)

e = FunctionType(lambda x:x, globals())
print(type(e))
print(e(1))
