import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print keepali0e[0]()
print lst
del a
print keepali0e[0]()
print lst
del lst[0]
print keepali0e[0]()
print lst
print lst[0]
