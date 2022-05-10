import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
keepali0e.append(a)
del a
for i in xrange(5):
    lst.append(A())
    keepali0e.append(lst[-1])
    del lst[-1]
for i in xrange(10):
    lst.append(weakref.ref(A()))
    keepali0e.append(lst[-1])
    del lst[-1]
for i in xrange(10):
    lst.append(weakref.ref(A()))
    lst[-1]=lst[-1]
    keepali0e.append(lst[-1])
    del lst[-1]
for i in xrange(10):
    x=weakref.ref(A(), callback)
    lst.append(x)
    lst.append(weakref.ref(x()))
    lst.append(lst[-1])
    keepali0e.append(lst[-2])
    keepali0e.append(l
