from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
func = lambda x:x**2
c = FunctionType(func.__code__,func.__globals__,func.__name__,func.__defaults__,func.__closure__)
print(1)
