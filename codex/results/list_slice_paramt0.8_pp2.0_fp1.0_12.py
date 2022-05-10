import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
lst

A=A()
B=A()
closer1e(A)

import gc
gc.collect()

class E(object):pass
e=E()
keepali0e.append(weakref.ref(e))
del e
keepali0e[0]()
keepali0e[0]().c
keepali0e[0]().c.c.c
keepali0e[0]().c.c.c.c
len(keepali0e)
lst
keepali0e
keepali0e[0]()
try:
    keepali0e[0]().c.c.c.c.c
except AttributeError:
    print 'attribute error'
lst
lst[0]
lst[0]==''
lst[0] is ''
lst[0] is not ''
type(lst[0])
type(str())

class F(object):pass
f=F()
keepali0e.append(weakref.ref(f,callback
