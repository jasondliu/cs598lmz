import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=()
a.d+=(a)
a.e=a
a.f=()
a.f+=(a)
a.h=[]
a.h+=(a)
for i in (1,A()):
    a.__dict__['%d'%i]=(a)
    a.__dict__['g%d'%i]=()
    a.__dict__['g%d'%i]+=(a)
lst+=(str())
lst+=(a)
lst+=(a)
import weakref
r=weakref.ref(a,callback)
del a
assert r() is None
