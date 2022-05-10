from types import FunctionType
a = (x for x in [1])
a.__next__
# for i in dir(a):
# 	print(i)
print(FunctionType.__mro__)
