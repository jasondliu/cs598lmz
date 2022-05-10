from types import FunctionType
a = (x for x in [1])
print(isinstance(a, Iterable))

#可调用的
print(isinstance(abs, Callable))
print(isinstance(abs, FunctionType))

#typ
