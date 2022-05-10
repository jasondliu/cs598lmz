import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(A())
keepalive=[]
for i in range(16):
    o = A()
    o.c = o
    lst.append(o)
    keepalive.append(o)
