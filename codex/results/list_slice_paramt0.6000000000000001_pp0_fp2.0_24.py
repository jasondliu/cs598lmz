import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
lst.append(a)
lst[1].c=lst
lst[1].c=lst
print keepali0e[0](),lst[0]

import gc
gc.collect()
print keepali0e[0]()
