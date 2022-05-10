from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(FunctionType))

def func(x,y):
    return x+y
print(type(func))
print(type(lambda x,y:x+y))
