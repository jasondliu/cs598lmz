import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=lst
b=A()
b.b=a
c=A()
c.a=b
keepalive=[a,b,c]
del b
del c
lst[0]=a
callback_obj=weakref.ref(a,callback)
del a
