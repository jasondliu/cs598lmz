import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
for i in xrange(1000):
    a=A()
    a.c=a
    a.s=lst
    a.s.append(a.s)
    weakref.ref(a.s,callback)
    a.s.append(a)
