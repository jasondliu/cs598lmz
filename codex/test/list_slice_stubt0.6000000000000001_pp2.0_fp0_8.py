import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
a.a=a
keepalive=[]
for i in range(1,200):
    a=A()
    a.a=a
    a.b=a
    a.c=a
    w=weakref.ref(a,callback)
    keepalive.append(a)
    keepalive.append(w)
    keepalive.append(w)
    del a
del keepalive
