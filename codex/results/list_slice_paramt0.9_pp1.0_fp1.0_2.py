import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a, callback))
a
lst
del a
keepalive
lst
class KeepAliveObject(object):
    def __init__(self):
        self.list=[]
    def __del__(self):
        del self.list
        print 'I got garbage-collected'
a=KeepAliveObject();
b=KeepAliveObject();
a.list.append(b)

a.list[0]



sys.getrefcount(a)
del b
sys.getrefcount(a)
a
import weakref;import gc;
a=KeepAliveObject()
b=KeepAliveObject()
del gc.collect()
sys.getrefcount(a)
a.list.append(b)
del b
a.list
 
 

sys.getrefcount(a)
 
gc.collect()
a
 
 


 


class CachedObject(object):
    def __init__(self):
        self.value=0

glob_cache=[]
_modulo=4

