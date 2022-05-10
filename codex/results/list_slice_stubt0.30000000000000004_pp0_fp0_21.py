import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
gc.collect()
lst.append(weakref.ref(lst,callback))
print len(lst)
del lst
gc.collect()
print len(keepalive)
keepalive[0].c=None
gc.collect()
print len(keepalive)

import weakref
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
gc.collect()
lst.append(weakref.ref(lst,callback))
print len(lst)
del lst
gc.collect()
print len(keepalive)
keepalive[0].c=None
gc.collect()
print len(keepalive)
