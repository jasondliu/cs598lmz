import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.a=str()
a.b=str()
a.d=a
keepalive=lst
keepalive.append(a)
lst.append(callback)
del keepalive
del lst
