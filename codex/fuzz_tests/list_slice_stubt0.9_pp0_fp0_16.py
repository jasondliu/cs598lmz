import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a.b=a.a=a
a.a()
print('a.c')
a.c=lst
a.d=lst
print('lst')
a.d(callback)
print('callback')
a.e=weakref.ref(a)
a.e().a.f=lst
a.e().a.f(callback)
