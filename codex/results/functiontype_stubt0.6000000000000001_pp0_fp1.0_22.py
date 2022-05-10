from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))

b = lambda x:x
print(b)
print(type(b))
print(isinstance(b, FunctionType))

c = lambda: None
print(c)
print(type(c))

d = lambda x=None: x
print(d)
print(type(d))

e = lambda x=None, y=None: x+y
print(e)
print(type(e))
