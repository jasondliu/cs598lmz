import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
keepali0e.append(weakref.ref(lst[0],callback))
lst=[]
</code>
In my case, the callback will be called immediately. I'm using CPython 2.6.6 on 32-bit Windows XP.

