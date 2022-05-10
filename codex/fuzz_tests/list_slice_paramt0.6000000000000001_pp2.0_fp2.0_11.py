import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
print lst
keepali0e.append(weakref.ref(a,callback))
del a
print lst
import sys
print sys.getrefcount(lst[0])
