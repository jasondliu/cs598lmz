from types import FunctionType
a = (x for x in [1])
print a
print a.__class__
print type(a)
print isinstance(a, FunctionType)
print dir(a)
