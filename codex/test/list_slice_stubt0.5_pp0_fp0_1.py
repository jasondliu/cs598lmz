import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
a.a=a
a.d=a
a.e=a
a.f=a
a.g=a
a.h=a
a.i=a
a.j=a
a.k=a
a.l=a
a.m=a
a.n=a
a.o=a
a.p=a
a.q=a
a.r=a
a.s=a
a.t=a
a.u=a
a.v=a
a.w=a
a.x=a
a.y=a
a.z=a
keepalive=[]
for i in range(100):
	keepalive.append(weakref.ref(a,callback))
del keepalive
del a
