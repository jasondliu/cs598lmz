from types import FunctionType
a = (x for x in [1])
print(a)

def f():
    return 3,5

a = f()
print(a)
print(type(3))
print(type(3,)==type(3))
print(type(f()) == type(3))
print(type(f) == FunctionType)
print(type([1,2]))
print(type([1,2])==list)
