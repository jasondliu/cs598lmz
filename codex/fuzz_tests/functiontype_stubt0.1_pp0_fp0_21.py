from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))
print(type(a.__iter__))
print(type(a.__next__) == FunctionType)
print(type(a.__iter__) == FunctionType)

print(dir(a))
print(dir(a.__next__))
print(dir(a.__iter__))

print(a.__next__.__name__)
print(a.__iter__.__name__)

print(a.__next__.__code__)
print(a.__iter__.__code__)

print(a.__next__.__code__.co_argcount)
print(a.__iter__.__code__.co_argcount)

print(a.__next__.__code__.co_varnames)
print(a.__iter__.__code__.co_varnames)

print(a.__next__.__code__.co_freevars)
print(a.__iter__.__code__.co_free
