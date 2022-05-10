import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=lst
a.e=callback
keepalive=[]
keepalive.append(a)
keepalive.append(a.c)
keepalive.append(a.d)
keepalive.append(keepalive)
lst.append(a)
lst.append(keepalive)
del a
del lst
gc.collect()
