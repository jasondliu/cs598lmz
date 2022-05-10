import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a.b=a.a=a
lst.append(a)
keepali0e.append(weakref.ref(a,callback))
del a,lst
keepali0e[0]()
try:
    import gc
    gc.collect()
except:
    pass
else:
    raise Exception("reference cycle not cleaned up")

import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a.b=a.a=a
lst.append(a)
keepali0e.append(weakref.ref(a,callback))
del a,lst
keepali0e[0]()
try:
    import gc
    gc.collect()
except:
    pass
else:
    raise Exception("reference cycle not cleaned up")

import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a
