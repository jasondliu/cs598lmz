from types import FunctionType
a = (x for x in [1])
print(a)
aa = FunctionType(a)
print(aa)
