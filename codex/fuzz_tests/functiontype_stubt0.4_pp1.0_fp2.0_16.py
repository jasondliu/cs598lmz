from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, FunctionType))

def func(x):
    return x

print(isinstance(func, FunctionType))

def func2():
    pass

print(isinstance(func2, FunctionType))

print(isinstance(map, FunctionType))

print(isinstance(lambda x: x, FunctionType))

print(isinstance(lambda: None, FunctionType))

print(isinstance(lambda x=None: None, FunctionType))

print(isinstance(lambda x=None, y=None: None, FunctionType))

print(isinstance(lambda x=None, *args: None, FunctionType))

print(isinstance(lambda x=None, *args, **kwargs: None, FunctionType))

print(isinstance(lambda x=None, *args, y=None, **kwargs: None, FunctionType))

print(isinstance(lambda x=None, *args, y=None, **kwargs: None, FunctionType))

print(isinstance(lambda x=None, *
