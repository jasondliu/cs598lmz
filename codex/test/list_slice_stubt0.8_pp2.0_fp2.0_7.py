import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
b=A()
b.c=b
keepalive=[a,b,lst]
lst[0]=a
lst[0]=a
a.c=b
a.c=b
b.c=a
b.c=a
b.c=b
b.c=b
a=A()
setattr(a,"__del__",callback)
lst[0]=a
a=b=None
for i in range(100):pass
