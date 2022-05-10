import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=[1,2,a,a]
lst.append(a)
keepalive.append(a)
del a
gc.collect()
