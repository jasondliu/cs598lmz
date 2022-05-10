import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a.b=a.a=a
keepalive.append(a)
keepalive.append(a.a)
keepalive.append(a.b)
keepalive.append(a.c)
x1=weakref.ref(a.a,callback)
x2=weakref.ref(a.b,callback)
x3=weakref.ref(a.c,callback)
del x1
del x2
del x3
del lst
