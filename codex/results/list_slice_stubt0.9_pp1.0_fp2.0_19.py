import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a.b=a.a=a.d=a.e=a.f=a.g=a.h=a.i=a.j=a.k=a
keepalive.append(a)
for p in xrange(18):
    r=weakref.ref(lst,callback)
    del r
    print len(lst), gc.collect(),
