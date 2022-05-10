from types import FunctionType
a = (x for x in [1])
print(type(a))

def my_func():
    pass

print(type(my_func))
print(isinstance(my_func, FunctionType))

print(isinstance(my_func, (FunctionType, int, float, str)))

print(isinstance([1, 2, 3], (str, list, tuple)))
