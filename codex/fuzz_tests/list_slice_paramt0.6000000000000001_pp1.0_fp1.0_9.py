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
keepali0e.append(weakref.ref(a,callback))
del lst,a
print keepali0e[0](),keepali0e[1](),keepali0e[2](),keepali0e[3]()
