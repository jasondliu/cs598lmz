from types import FunctionType
a = (x for x in [1]).__iter__
print(a)
print(a.__class__)
print(type(a))
print(isinstance(a, FunctionType))
print(FunctionType)

print(dir(a))
print(a.__call__)
print(a.__self__)
print(a.__qualname__)
print(a.__class__.__qualname__)
print(a.__class__.__name__)
print(a.__name__)
print(a.__annotations__)
print(a.__objclass__)
# print(a.func_closure)
# print(a.__closure__)
# print(a.__dir__)
print(a.__defaults__)
print(a.__dict__)
print(a.__doc__)
print(a.__get__)
print(a.__globals__)
a.__hash__
print(a.__init__)
print(a.__kwdefaults__)
print(a.__module__)
print(a.__name__)
