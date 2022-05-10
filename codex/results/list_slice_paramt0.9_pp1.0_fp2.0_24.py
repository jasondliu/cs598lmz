import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepalive=[]
lst=[str()]
a=A()
keepali0e.append(weakref.ref(a,callback))
del a
import gc
gc.collect()
len(lst)

def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
import gc
gc.collect()
len(lst)

def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
keepali0e.append(weakref.ref(a,callback))
del a
import gc
gc.collect()
len(lst)

import weakref
class A(object):pass
def callback(x):del lst[0]
lst=[A()]
weakref.ref(lst[0],callback)
import gc
gc.collect()
len(lst)
