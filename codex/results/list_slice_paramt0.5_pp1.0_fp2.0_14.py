import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
lst.append(weakref.ref(a,callback))
del a
print(len(lst))
print(lst[0])
print(lst[1])
print(lst[1]())
print(lst[1]().c)
print(lst[1]().c.c)
print(keepali0e[0]())
print(keepali0e[0]().c)
print(keepali0e[0]().c.c)
print(lst[1]())
print(lst[1]().c)
print(lst[1]().c.c)
print(keepali0e[0]())
print(keepali0e[0]().c)
print(keepali0e[0]().c.c)
print(lst[1]())
print(lst[1]().c)
print(lst[1]().c.c)
print(keepali0e[0]())
print(keepali0e[0]().c)
print(keepali0e[0](
