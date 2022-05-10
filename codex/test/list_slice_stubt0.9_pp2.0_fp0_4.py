import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a #self-reference
keepalive=a
b=[a,lst]
c=[lst,b]
del a
del b
del lst
