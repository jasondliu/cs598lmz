import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
del a
keepali0e.append(weakref.ref(lst[0],callback))
print len(keepali0e)
print len(keepali0e)
print len(keepali0e)
print len(keepali0e)
print len(keepali0e)
print len(keepali0e)
