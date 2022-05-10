from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(type(a.__next__))

print(type(1))
print(type(int))
print(int.__call__)
print(type(int.__call__))
print(int.__call__(1))
print(int(1))
print(int.__call__(1, base=2))
print(int(1, base=2))
print(type(int.__call__))
print(type(int.__call__.__call__))

print(int.__call__.__call__.__call__)
print(type(int.__call__.__call__.__call__))
print(int.__call__.__call__.__call__(1))
print(int.__call__.__call__.__call__.__call__(1))
print(int.__call__.__call__.__call__.__call__.__call__(1))
print(int.__call__.__call__.__call__.__call__.
