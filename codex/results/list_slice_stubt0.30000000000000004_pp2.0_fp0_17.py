import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a.c=None
lst[0]=a
keepalive.append(lst)
keepalive.append(callback)
weakref.ref(a,callback)
del a
del keepalive
del lst
</code>

