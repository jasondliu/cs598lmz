import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
print("Delay gc")
keepali0e.append(weakref.ref(a.c))
lst[0]=a
print("Make a strongly referenced")
lst[0].other=a
print("Delay cyclic gc")
keepali0e.append(weakref.ref(lst[0].other))
keepali0e.append(weakref.ref(a.c.other))
keepali0e.append(weakref.ref(a.c.other.c))
keepali0e.append(weakref.ref(a.c.other.c.other))
del a
expectException(RuntimeError)
del a.c
expectException(RuntimeError)
keepali0e[:] = []
#expectException(AttributeError)
del lst[0].other
