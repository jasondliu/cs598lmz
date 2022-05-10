import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepali0e.append(weakref.ref(lst,callback))
del a
del lst
import gc
gc.collect()
print keepali0e[0]()
lst=[str()]
lst.append(lst)
keepali0e.append(weakref.ref(lst,callback))
del lst
gc.collect()
print keepali0e[1]()
lst=[str()]
keepali0e.append(weakref.ref(lst,callback))
del lst
gc.collect()
print keepali0e[2]()
lst=[str()]
lst.append(lst)
keepali0e.append(weakref.ref(lst,callback))
del lst
gc.collect()
print keepali0e[3]()
lst=[str()]
lst.append(lst)
keepali0e.append(weakref.ref(lst,callback))
del lst
gc.collect()
print keepali0e[4]()
