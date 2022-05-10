import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive=[a]
a.a=weakref.ref(a,callback)
a.a()
class B(object):pass
b=B()
b.c=b
keepalive.append(b)
b.b=weakref.ref(b,callback)
b.b()
del a,b,keepalive
