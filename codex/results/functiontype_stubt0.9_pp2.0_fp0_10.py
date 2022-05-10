from types import FunctionType
a = (x for x in [1])
print type(a)
print type((x for x in [1]))
print type(lambda x:x+2)
print type(FunctionType)
