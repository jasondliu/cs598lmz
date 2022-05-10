import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
a.c=a
del a
print lst.pop()
print keepali0e.pop()
print lst[0]
print keepali0e[0]()
