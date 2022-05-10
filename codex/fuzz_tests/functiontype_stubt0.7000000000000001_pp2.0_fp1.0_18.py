from types import FunctionType
a = (x for x in [1])
print type(a)
print type(a.next)
print type(a.__iter__)
print type(a.__getitem__)
print type(a.__getslice__)

print type([]), type(list)
print type(())
print type({})
print type(set())
print type(frozenset())
print type(dict())

print type(int)
print type(type)

print type(a.next) == FunctionType
