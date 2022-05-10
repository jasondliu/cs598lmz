import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=a
keepalive.append(a)
for i in xrange(10):
    a=A()
    keepalive.append(a)
    lst.append(a)
    lst[-1].callback=weakref.ref(lst[-1],callback)
print len(lst)
for i in xrange(100000):
    a=A()
    keepalive.append(a)
    lst.append(a)
    lst[-1].callback=weakref.ref(lst[-1],callback)
print len(lst)
