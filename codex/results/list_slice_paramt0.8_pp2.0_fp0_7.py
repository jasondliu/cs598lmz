import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
del a.c
print keepali0e[0]()
a=A()
a.keepali0e=a
keepali0e.append(weakref.ref(a))
del a.keepali0e
print keepali0e[1]()
a=A()
a.keepali0e=a
keepali0e.append(weakref.ref(a))
del a.keepali0e
print keepali0e[2]()
a=A()
a.keepali0e=a
keepali0e.append(weakref.ref(a,callback))
del a.keepali0e
print keepali0e[3]()
a=A()
a.keepali0e=a
keepali0e.append(weakref.ref(a,callback))
del a.keepali0e
print keepali0e[4]()
a=A()
a.keepali0e=a
keepali0e.append(weakref.ref(a,callback))
del a.keepali0e
print keepali0e[
