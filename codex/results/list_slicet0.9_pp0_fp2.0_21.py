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
A.c=A()
A.c.c=A.c
keepali0e.append(weakref.ref(A.c,callback))
del A.c
while lst:keepali0e.append(lst[:])
del lst, keepali0e

c=Node()
d=Node()
c.data=d
d.data=c
weakref.ref(c,callback)
weakref.ref(d,callback)
del c, d
while lst:keepali0e.append(lst[:])
del lst, keepali0e, callback
