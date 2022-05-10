import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=100
keepalive=[a,a.c,a.b,lst,A]
lst[0]=a
