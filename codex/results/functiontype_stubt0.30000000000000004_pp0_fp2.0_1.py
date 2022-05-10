from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__iter__))
print(type(a.__next__))
print(type(a.__next__()) == int)
print(type(a.__next__) == FunctionType)
print(type(a.__next__) == type(a.__iter__))

print(a.__next__.__self__)
print(a.__next__.__self__.__next__)
print(a.__next__.__self__.__next__ == a.__next__)
print(a.__next__.__self__.__next__ == a.__next__.__self__.__next__)

print(a.__next__.__self__.__iter__)
print(a.__next__.__self__.__iter__ == a.__iter__)
print(a.__next__.__self__.__iter__ == a.__next__.__self__.__iter__)

print(a.__next__.__self__.__iter__ == a.
