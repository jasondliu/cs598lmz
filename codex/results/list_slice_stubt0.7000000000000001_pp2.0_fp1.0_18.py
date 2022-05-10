import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(weakref.ref(a,callback))
keepalive.append(a)
del a
del lst
import gc
gc.collect()
time.sleep(3)

import weakref
callback=[]
def callback(x):print 'callback'
lst=[str()]
a=str()
a=str()
lst.append(weakref.ref(a,callback))
a=str()
del a
del lst
import gc
gc.collect()
