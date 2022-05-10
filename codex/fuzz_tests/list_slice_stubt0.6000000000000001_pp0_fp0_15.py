import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
a.x=lst
a.y=lst
a.z=lst
a.t=lst
keepalive.append(a)
del a
gc.collect()
lst=[]
gc.collect()
a=A()
a.c=a
a.b=a
a.x=lst
a.y=lst
a.z=lst
a.t=lst
keepalive.append(a)
del a
gc.collect()
a=A()
a.c=a
a.b=a
a.x=lst
a.y=lst
a.z=lst
a.t=lst
keepalive.append(a)
del a
gc.collect()
a=A()
a.c=a
a.b=a
a.x=lst
a.y=lst
a.z=lst
a.t=lst
keepalive.append(a)
del a
gc.collect()
