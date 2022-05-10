import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.proxy(a.c))
print(a.c is keepali0e[0])
print(a.c is a)
print(a.c is keepali0e[0])
del a
print(lst)
weakref.ref(lst,callback)
del lst
print(keepali0e)
lst=[]
a=A()
lst.append(a)
a.c=a
keepali0e.append(weakref.proxy(a.c))
print(a.c is keepali0e[0])
print(a.c is a)
print(a.c is keepali0e[0])
del lst
print(keepali0e)
