import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a.c=lst
keepalive.append(a)
del a
del keepalive
for i in xrange(10000):
    a=A()
    a.c=lst
    wr=weakref.ref(a,callback)
    del a
    gc.collect()
    print lst[0]
    print wr()
    print len(gc.get_referrers(lst))
    print len(gc.get_referrers(lst[0]))
    print len(gc.get_referrers(wr))
    print len(gc.get_referrers(wr()))
    print len(gc.get_referrers(callback))
