from types import FunctionType
a = (x for x in [1])
b = (x for x in [2])
a.send(None)
b.send(None)
print(a.gi_frame.f_lasti)
print(b.gi_frame.f_lasti)

def func(a):
    print(a)

print(type(func))
print(FunctionType)
print(isinstance(func, FunctionType))

def func(a):
    print(a)

print(func.__name__)
print(func.__qualname__)
print(func.__doc__)
print(func.__module__)
print(func.__defaults__)
print(func.__code__)
print(func.__globals__)
print(func.__dict__)
print(func.__closure__)
print(func.__annotations__)
print(func.__kwdefaults__)

print(func.__call__)
print(func.__get__)
print(func.__set__)
print(func.__delete__)

def func(a):
