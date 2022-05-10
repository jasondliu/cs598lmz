from types import FunctionType
a = (x for x in [1])
print(type(a))

b = [x for x in [1,2,3]]
print(type(b))

c = {x for x in [1,2,3]}
print(type(c))

d = {x:x for x in [1,2,3]}
print(type(d))

e = FunctionType(lambda x:x+1,globals())
print(type(e))
print(e(1))
print(e(2))
print(e(3))
