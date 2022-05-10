import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
del keepalie
lst=[str()]
a=A()
b=A()
a.c=b
b.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(b,callback))
del a
del b
while lst:keepali0e.append(lst[:])
del keepalie
lst=[str()]
a=A()
b=A()
c=A()
a.c=c
b.c=c
c.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(b,callback))
keepali0e.append(weakref.ref(c,callback))
del a
del b
del c
while lst:keepali0e.append(lst[:])
del keepalie
lst=[str()]
a=A()
b=A()
c=A()
d=A()
a.c=d
b.c
