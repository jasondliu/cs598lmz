import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
del a
print(lst)
print(keepali0e)
print(keepali0e[0]())
del lst
print(keepali0e)
print(keepali0e[0]())
