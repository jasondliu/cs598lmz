import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive=a
del a
del keepalive
lst=None
del lst
A()
lst=[]
del lst
