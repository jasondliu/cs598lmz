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
print keepali0e
class C(object):pass
c=C()
c.b=c
lst=[str()]
keepali0e=[]
keepali0e.append(weakref.ref(c,callback))
del c
while lst:keepali0e.append(lst[:])
print keepali0e
