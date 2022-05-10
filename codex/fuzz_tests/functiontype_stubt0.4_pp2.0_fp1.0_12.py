from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__iter__))
print(type(a.__next__))
print(type(a.__next__()))

def func():
    pass

print(type(func))
print(type(func.__call__))
print(type(func.__call__()))

print(type(FunctionType))
print(type(FunctionType.__call__))
print(type(FunctionType.__call__()))
