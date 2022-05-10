import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
keepali0e.append(weakref.ref(lst[0],callback))
del keepali0e
lst[0]="foo"
import gc
gc.collect()
print len(lst)
