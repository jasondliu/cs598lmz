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
lst=[str()]
b=A()
b.c=b
keepali0e.append(weakref.ref(b,callback))
del b
while lst:keepali0e.append(lst[:])
lst=[str()]
c=A()
c.c=c
keepali0e.append(weakref.ref(c,callback))
del c
while lst:keepali0e.append(lst[:])
lst=[str()]
d=A()
d.c=d
keepali0e.append(weakref.ref(d,callback))
del d
while lst:keepali0e.append(lst[:])
lst=[str()]
e=A()
e.c=e
keepali0e.append(weakref.ref(e,callback))
del e
while lst:keepali0e.append(lst[:])
lst=[str()]
f=A()
f.c=f
keepali0e.append(weakref.ref(f,callback))
