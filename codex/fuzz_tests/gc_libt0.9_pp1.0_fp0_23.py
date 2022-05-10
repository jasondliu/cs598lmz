import gc, weakref, sys
class ReferenceableThing(object):
    pass

a = ReferenceableThing()
# b = a
# c = a
print(a, sys.getrefcount(a))
print(a, sys.getrefcount(a)-1)
# print(b, sys.getrefcount(b))
# print(c, sys.getrefcount(c))

d = weakref.ref(a)
e = weakref.ref(a)
gc.collect()
print(a, sys.getrefcount(a)-1)
# print(b, sys.getrefcount(b))
# print(c, sys.getrefcount(c))
print(d, d())
print(e, e())

del a
# del b
# del c
gc.collect()
print(d, d())
print(e, e())
