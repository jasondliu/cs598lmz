import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
keepali0e.append(weakref.ref(a.c))
keepali0e.append(weakref.ref(lst))
keepali0e.append(weakref.ref(lst[0]))
keepali0e.append(weakref.ref(callback))
keepali0e.append(weakref.ref(keepali0e))
keepali0e.append(weakref.ref(keepali0e[0]))
keepali0e.append(weakref.ref(keepali0e[1]))
keepali0e.append(weakref.ref(keepali0e[2]))
keepali0e.append(weakref.ref(keepali0e[3]))
keepali0e.append(weakref.ref(keepali0e[4]))
keepali0e.append(weakref.ref(keepali0e[5]))
keepali0e.append(weakref.ref(keepali0e[6]))
keepali0e.append(weakref.ref(keepali0e[7]))
