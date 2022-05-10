from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__iter__))
print(type(a.__next__))
print(type(a.__next__) == FunctionType)

print(dir(a))
print(dir(a.__iter__))
print(dir(a.__next__))

print(a.__iter__.__class__)
print(a.__next__.__class__)

print(a.__iter__.__class__ == FunctionType)
print(a.__next__.__class__ == FunctionType)

print(a.__iter__.__class__ == type(a.__iter__))
print(a.__next__.__class__ == type(a.__next__))

print(a.__iter__.__class__ == type(a.__iter__.__call__))
print(a.__next__.__class__ == type(a.__next__.__call__))

print(a.__iter__.__class__ == type(a.__iter__.__call__.__
