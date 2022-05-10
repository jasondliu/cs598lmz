import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a;
a.e=a;
a.d=a;
a.b=a;
a.f=a;
a.a=a;
for i in range(1000):
   keepali0e.append(weakref.ref(a,callback));

lst=None
del keepali0e
