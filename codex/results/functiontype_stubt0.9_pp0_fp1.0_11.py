from types import FunctionType
a = (x for x in [1])
b = [lambda :1]
print(a)
print(type(a))
print(a.__next__()) # >>> 1
print(a.__next__()) # >>> StopIteration:

#l = [1,2,3,4]
#it = iter(l)
#print(it.__next__()) # >>> 1
#print(it.__next__()) # >>> 2
#print(it.__next__()) # >>> 3
#print(it.__next__()) # >>> 4
#print(it.__next__()) # >>> StopIteration:
