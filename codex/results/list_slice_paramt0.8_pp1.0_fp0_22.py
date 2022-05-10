import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a, callback))
print len(lst)
del a, keepali0e
import gc;gc.collect()
print len(lst)
print len(gc.get_referrers(lst))
