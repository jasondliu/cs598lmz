import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.p=a
a.t=a
keepalive=[a,a.c,a.p,a.t,a.c.c,a.c.p,a.c.t,a.p.c,a.p.p,a.p.t,a.t.c,a.t.p,a.t.t]
keepalive=[weakref.ref(o,callback)for o in keepalive]
del keepalive
f()
print(lst)
