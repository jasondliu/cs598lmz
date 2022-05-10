import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
keepali0e.append(weakref.ref(a,callback))
del a
a=lst[1]
del lst[1]
print(bool(keepali0e[0]()))
print(bool(keepali0e[1]()))
