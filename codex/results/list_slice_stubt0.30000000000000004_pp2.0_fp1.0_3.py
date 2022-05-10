import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst[0]=weakref.ref(a,callback)
del a
gc.collect()
print lst

#[<weakref at 0x0000000002A8A908; to 'A' at 0x0000000002A8A828>]

import weakref
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst[0]=weakref.ref(a,callback)
del a
gc.collect()
print lst

#[<weakref at 0x0000000002A8A908; dead>]

import weakref
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst[0]=weakref.ref(a,callback)
del a
gc.collect()
print
