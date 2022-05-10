import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
keepali0e.append(weakref.ref(a.c))
keepali0e.append(weakref.ref(lst[0]))
keepali0e.append(str())
del a
del lst
weakref.ref(lst)
keepali0e.pop()
keepali0e.pop()
