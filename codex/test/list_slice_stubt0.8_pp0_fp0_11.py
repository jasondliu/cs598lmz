import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a.c
lst.append(a.b)
lst.append(a.c)
keepalive=lst
del lst
f=weakref.ref(a,callback)
del a
f()
