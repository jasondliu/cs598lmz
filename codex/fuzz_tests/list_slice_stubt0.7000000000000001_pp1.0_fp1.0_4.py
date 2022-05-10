import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
keepali0e.append([a,a.b,a.c])
del a
del keepalive[0]
callback(lst[0])
keepalive=[]
lst=[str()]
a=A()
a.c=a
a.b=a
keepalive.append([a,a.b,a.c])
del a
del keepalive[0]
callback(lst[0])
