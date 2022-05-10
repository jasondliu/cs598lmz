import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
a.c=None
del a
import gc
gc.collect()
print lst
print keepali0e

#Output:
['x']
[<weakref at 0x00CA0D88; dead>, <weakref at 0x00CA0DB8; dead>]
