import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
print(a.c)
print(keepali0e[0]())
print(str())

del lst[0]
print(a.c)
print(keepali0e[0]())
