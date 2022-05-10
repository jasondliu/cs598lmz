import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a.b=a.a=lst
lst.append(a)
cb1=weakref.ref(a,callback)
cb2=weakref.ref(a.a,callback)
cb3=weakref.ref(a.b,callback)
cb4=weakref.ref(a.c,callback)
keepalive.append(a)
keepalive.append(a.a)
keepalive.append(a.b)
keepalive.append(a.c)
keepalive.append(lst)
keepalive.append(cb1)
keepalive.append(cb2)
keepalive.append(cb3)
keepalive.append(cb4)
keepalive.append(callback)
print len(gc.get_referrers(a))
print len(gc.get_referrers(a.a))
print len(gc.get_referrers(a.b))
print len(gc.get_referrers(a.c))
print len(gc.get_referrers(lst))
print
