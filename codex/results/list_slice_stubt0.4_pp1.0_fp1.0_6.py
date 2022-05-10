import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=a
lst.append(a)
keepalive.append(lst)
lst.append(weakref.ref(lst,callback))
del a
del lst
gc.collect()
print(keepalive[0])

#output
[str(), <weakref at 0x00E5D5F8; to 'list' at 0x00E5D5D0>, <weakref at 0x00E5D638; dead>]

#example 3
import gc
import weakref
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.c=a
a.d=a
lst.append(a)
keepalive.append(lst)
lst.append(weakref.ref(lst,callback))
del a
del lst
gc.collect()
print(keepalive[0])

#output
[str(), <weakref at 0x00E5D5F8; to 'list
