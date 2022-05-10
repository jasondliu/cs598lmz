import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a.d=a.e=a
a.f=lambda :a
a.g=lst
a.h=keepalive
a.i=callback
a.j=lst
a.k=str()
keepalive.append(a)
del a
print(lst)
