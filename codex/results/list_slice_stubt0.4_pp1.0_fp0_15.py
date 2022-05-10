import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
del a
import gc
gc.collect()
print lst

#lst=['',<weakref at 0x7f1d0f8c8f38; to 'A' at 0x7f1d0f8c8f10>]

#callback函数是在gc的时候调用的，所以gc的时候不会被回收

#第二种情况，循环引用
import weakref
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
del a
import gc
gc.collect()
print lst

#lst=['
