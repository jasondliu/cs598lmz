import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c))
keepali0e.append(weakref.ref(a,callback))
print lst, len(keepali0e)
del a
print lst, len(keepali0e)
print keepali0e[0]()
