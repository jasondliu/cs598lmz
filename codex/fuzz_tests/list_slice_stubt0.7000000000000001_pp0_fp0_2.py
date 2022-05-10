import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
print(id(lst[0]),id(lst[1]))
keepali0e.append(weakref.ref(lst[0],callback))
keepali0e.append(weakref.ref(lst[1],callback))
del a
del lst
print(keepali0e)
