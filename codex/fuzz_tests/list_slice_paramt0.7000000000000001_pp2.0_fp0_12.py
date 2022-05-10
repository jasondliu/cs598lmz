import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print(len(lst))
del a
import gc
gc.collect()
print(len(lst))

lst=[]
a=A()
lst.append(a)
a.c=a

a.b = weakref.ref(a.c,callback)
del a
import gc;gc.collect()
print(len(lst))
