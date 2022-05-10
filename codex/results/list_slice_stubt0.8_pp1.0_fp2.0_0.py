import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=lst
keepalive.append(a)
del a
lst.append(a)
del lst
cb=weakref.ref(callback)
print cb()
