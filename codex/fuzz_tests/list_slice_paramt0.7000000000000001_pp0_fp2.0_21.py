import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
a.b=[a]
while len(lst):
    pass
del a
keepali0e.append(weakref.ref(a,callback))
a=A()
keepali0e.append(weakref.ref(a,callback))
a.b=[a]
a.c=a
del a
keepali0e.append(weakref.ref(a,callback))
a=A()
a.b=[a]
a.c=a
keepali0e.append(weakref.ref(a,callback))
a=A()
a.b=[a]
a.c=a
keepali0e.append(weakref.ref(a,callback))
a=A()
a.b=[a]
a.c=a
keepali0e.append(weakref.ref(a,callback))
a=A()
a.b=[a]
a.c=a
keepali0e.append(weakref.ref(a,callback))
a=A()
a.b=[a]
a.c=a

