import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive=[a]
for i in xrange(1000):
    a.a=str()
    b=A()
    b.a=a
    b.c=b
    a=b
    keepalive.append(b)
del a
del b
for i in xrange(1000):
    a=A()
    a.c=a
    keepalive.append(a)
del a
for i in xrange(1000):
    a=A()
    a.a=a
    a.c=a
    keepalive.append(a)
del a
for i in xrange(1000):
    a=A()
    a.a=str()
    a.b=a
    a.c=a
    keepalive.append(a)
del a
for i in xrange(1000):
    a=A()
    a.a=str()
    a.b=a
    b=A()
    b.a=a
    b.c=b
    keepalive.append(b)
del a
