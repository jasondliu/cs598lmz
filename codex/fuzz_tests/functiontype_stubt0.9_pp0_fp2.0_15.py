from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)

c = {x for x in [1]}
d = {x for x in [1]}
print(c == d)

print((lambda *e: None).__code__ is (lambda *e: None).__code__)
print(lambda *e: None == lambda: None)
print(type(type))
print(type(print))         # type()
print(type(FunctionType))  # types.FunctionType

print(type.__dict__['__call__'] is FunctionType.__call__)
