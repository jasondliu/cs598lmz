import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
lst.append(a)
del a
lst.append(callback)
def g():lst[0]()
g()
g()
g()
g()
print keepali0e
