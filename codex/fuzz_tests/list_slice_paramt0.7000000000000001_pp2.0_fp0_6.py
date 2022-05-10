import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a, callback))
a.b=lst
lst=None
print 'kept alive by', len(keepali0e), 'references'
print '   ', keepali0e[0]()
del a
import gc
gc.collect()
print 'kept alive by', len(keepali0e), 'references'
print '   ', keepali0e[0]()

# As you can see, the callback deleted the reference in the list, leading to the fact that the cycle is broken and the object can be deleted.
