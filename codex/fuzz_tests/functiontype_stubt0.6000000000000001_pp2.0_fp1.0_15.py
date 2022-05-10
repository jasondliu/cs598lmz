from types import FunctionType
a = (x for x in [1])
print(type(a))

def fn():
    pass

b = FunctionType(a, globals())
print(b)
print(type(b))
