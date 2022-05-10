from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))
print(type(a.__iter__))
print(type(a.__next__) == type(a.__iter__))
print(type(a.__next__) == FunctionType)
print(type(a.__iter__) == FunctionType)

print(a.__next__.__name__)
print(a.__iter__.__name__)

print(a.__next__.__qualname__)
print(a.__iter__.__qualname__)

print(a.__next__.__module__)
print(a.__iter__.__module__)

print(a.__next__.__class__)
print(a.__iter__.__class__)

print(a.__next__.__closure__)
print(a.__iter__.__closure__)

print(a.__next__.__code__)
print(a.__iter__.__code__)

print(a.__next__.__default
