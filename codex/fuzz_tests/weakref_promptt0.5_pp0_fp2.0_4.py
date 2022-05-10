import weakref
# Test weakref.ref()
import gc

class C(object):
    pass

o = C()
r = weakref.ref(o)
o2 = r()
print o is o2

del o
gc.collect()
o2 = r()
print o2 is None

# Test weakref.proxy()
class MyList(list):
    pass

lst = MyList(range(10))
p = weakref.proxy(lst)
print type(p) is MyList
print p is lst
print p == lst
print p[2] == lst[2]

lst = None
gc.collect()
try:
    p[2]
except ReferenceError:
    print "ReferenceError"

# Test weakref.getweakrefcount()
class C(object):
    pass

o = C()
r1 = weakref.ref(o)
r2 = weakref.ref(o)
print weakref.getweakrefcount(o)

# Test weakref.getweakrefs()
class C(object):
    pass


