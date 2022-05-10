import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
a.c=a
lst[0]=a
a.b=a
keepali0e.append(weakref.ref(a))
a.b=str()
a.a=str()
lst[0]=a
a.b=a
a.a=a
print(lst[0].a)
