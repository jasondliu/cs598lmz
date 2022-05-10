import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst[0]= a
keepalive.append(a)
callback.__dict__["__refs__"]=[weakref.ref(lst), weakref.ref(a)]
keepalive.append(callback)
del keepalive
</code>

