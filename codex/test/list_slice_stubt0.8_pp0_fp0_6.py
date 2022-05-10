import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=lst
a.e=keepali0e
keepali0e.append(weakref.ref(a,callback))
print(keepali0e)
keepali0e.append(lst)
keepali0e.append(keepali0e)
print(keepali0e)
del keepali0e
del a
del lst

import gc
collecteD_objects=gc.collect()
