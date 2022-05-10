import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(lst)
keepali0e.append(callback)
weakref.ref(a,callback)
del keepali0e
del a
del lst
del callback
gc.collect()
</code>
I'm using Python 2.7.3 (default, Apr 10 2012, 23:24:47) [MSC v.1500 64 bit (AMD64)] on win32
I'm not sure why it's happening. I'm using it in a game engine and it's causing a lot of trouble.

