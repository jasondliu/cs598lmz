import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
b=A()
b.c=a
keepalive=[a,b]
a.a_ref=weakref.ref(a,callback)
b.b_ref=weakref.ref(b,callback)
del a
del b
