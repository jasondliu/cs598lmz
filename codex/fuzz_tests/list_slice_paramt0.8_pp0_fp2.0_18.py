import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a,callback))
print(sys.getrefcount(a))
keepali0e.append(weakref.ref(a))
keepali0e.append(weakref.ref(a))
print(sys.getrefcount(a))
keepali0e.append(weakref.ref(a))
keepali0e.append(weakref.ref(a))
print(sys.getrefcount(a))
del a
del keepali0e
print(sys.getrefcount(lst))
del lst
