import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a.d=a.e=a.f=a.g=a.h=a.i=a.j=a.k=a.l=a.m=a.n=a.o=a.p=a.q=a.r=a.s=a.t=a.u=a.v=a.w=a.x=a.y=a.z=None
a.a=a.b=a.c
a.c=a.d=a.e=a.f=a.g=a.h=a.i=a.j=a.k=a.l=a.m=a.n=a.o=a.p=a.q=a.r=a.s=a.t=a.u=a.v=a.w=a.x=a.y=a.z=a
a.a=a.b=a.c
keepali0e.append(a)
weakref.ref(a,callback)
del a
print lst[0]
</code>

