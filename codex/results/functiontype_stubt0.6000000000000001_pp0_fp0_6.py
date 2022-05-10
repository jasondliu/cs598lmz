from types import FunctionType
a = (x for x in [1])
print(type(a))

def fn():
    pass

print(type(fn))
print(type(fn) == type(fn))
print(type(fn) == FunctionType)

print(isinstance(fn, FunctionType))
print(isinstance(fn, (FunctionType, list)))
print(isinstance(fn, (list, tuple)))
