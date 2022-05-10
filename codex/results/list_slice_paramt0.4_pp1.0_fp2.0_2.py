import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
for i in range(10):
    lst.append(str())
    keepali0e.append(weakref.ref(lst[-1],callback))
    del lst[-1]
print len(lst)
print len(keepali0e)
for i in range(10):
    lst.append(str())
    keepali0e.append(weakref.ref(lst[-1],callback))
    del lst[-1]
print len(lst)
print len(keepali0e)
print lst[0]
print keepali0e[0]()
print keepali0e[0]() is None
print keepali0e[0]() is None
print keepali0e[0]() is None
print keepali0e[0]() is None
print keepali0e[0]() is None
print keepali0e[0]() is None
print keepali0e[0]() is None
print keepali0e[0]() is None
print keepali0e[
