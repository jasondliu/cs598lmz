from types import FunctionType
a = (x for x in [1])
print(type(a))

def b():
    pass

print(type(b))
print(type(FunctionType))
print(FunctionType)

b.__name__ = 'jason'

print(b.__name__)
print(type(b))
print(type(FunctionType))
print(FunctionType)
print(type(range))
