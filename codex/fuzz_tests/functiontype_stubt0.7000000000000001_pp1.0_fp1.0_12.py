from types import FunctionType
a = (x for x in [1])
print(type(a))
b = [x for x in [1]]
print(type(b))
c = FunctionType(lambda : 1, globals())
print(type(c))
