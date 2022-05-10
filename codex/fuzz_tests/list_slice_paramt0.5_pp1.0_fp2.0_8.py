import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
lst.append(a)
lst.append(a.c)
del a
del a.c
import gc
gc.collect()
print(len(lst))
