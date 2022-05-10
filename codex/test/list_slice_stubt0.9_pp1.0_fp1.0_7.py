import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
weakref.ref(a,callback)
for i in range(100):
    a.d=A()
    a.d.c=a.d
    keepali0e.append(a.d.c)
    a.d=A()
    a.d.c=a.d
    keepali0e.append(a.d.c)
keepali0e.append(a)
