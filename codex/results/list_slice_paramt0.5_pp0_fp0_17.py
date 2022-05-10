import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
print(keepali0e[0]())
del a
print(keepali0e[0]())
lst[0]=A()
print(keepali0e[0]())
lst[0].c=lst[0]
print(keepali0e[0]())
keepali0e.append(weakref.ref(lst[0],callback))
print(keepali0e[1]())
del lst[0]
print(keepali0e[1]())
lst[0]=str()
print(keepali0e[1]())
lst[0]=A()
print(keepali0e[1]())
lst[0].c=lst[0]
print(keepali0e[1]())
del lst[0]
print(keepali0e[1]())
# print(keepali0e[1]())
