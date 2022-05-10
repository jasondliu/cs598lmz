import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a.d=a.e=a.f=a.g=a.h=a
a.b=lst
lst[0]=a
del a
gc.collect()
lst=lst[0].b
lst[0]=lst[0]
del lst[0]
lst[0]=lst[0]
del lst[0]
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.c=a.d=a.e=a.f=a.g=a.h=a
a.b=lst
lst[0]=a
del a
gc.collect()
lst=lst[0].b
lst[0]=lst[0]
del lst[0]
lst[0]=lst[0]
del lst[0]
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A
