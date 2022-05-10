import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))

A()
a.x=1

del  keepali0e
del lst
del a
del A
#import sys
#print sys.getrefcount(A())
#1
