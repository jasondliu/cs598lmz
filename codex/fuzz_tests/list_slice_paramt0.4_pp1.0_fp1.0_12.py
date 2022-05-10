import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst[0]=a
del a
print keepali0e
print lst
print len(keepali0e)
print len(lst)
print keepali0e[0]()
print lst[0]
print len(keepali0e)
print len(lst)
