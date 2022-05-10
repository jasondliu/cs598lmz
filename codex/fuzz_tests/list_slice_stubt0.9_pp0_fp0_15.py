import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
c=weakref.ref(lst[0],callback)
lst=None
import gc
for i in xrange(100):gc.collect()
print c()is None
print len(gc.garbage)
def delcycle():
    keepalive=[]
    lst=[]
    a=A()
    keepalive.append(a)
    lst.append(a)
    a.b=a
    lst.append(a)
    del a,lst
    for i in xrange(100):gc.collect()
    gc.garbage[0].b=gc.garbage[1]
    gc.garbage[1].b=gc.garbage[0]
    del keepalive
    for i in xrange(100):gc.collect()
delcycle()
print len(gc.garbage)
type(gc.garbage[0].b)

#20.16编码问题
class p(object):
    __slots
