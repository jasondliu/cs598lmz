from types import FunctionType
a = (x for x in [1])
b = []
def func():
    pass
print(type(a))
print(type(b))
print(type(func))
print(isinstance(func, FunctionType))
