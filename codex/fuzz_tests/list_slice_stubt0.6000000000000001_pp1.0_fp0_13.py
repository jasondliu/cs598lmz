import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=a
keepali0e.append(weakref.ref(a,callback))
a=0
del keepali0e
print lst
import sys
print sys.getrefcount(lst)
print sys.getrefcount(lst[0])
print sys.getrefcount(lst[0])
print sys.getrefcount(lst[0])
print sys.getrefcount(lst[0])
print sys.getrefcount(lst[0])
print sys.getrefcount(lst[0])
print sys.getrefcount(lst[0])
print sys.getrefcount(lst[0])
print sys.getrefcount(lst[0])
print sys.getrefcount(lst[0])
print sys.getrefcount(lst[0])
print sys.getrefcount(lst[0])
print sys.getrefcount(lst[0])
print sys.getrefcount(lst[0])
print sys.getrefcount(lst[0])
print sys.getrefcount(l
