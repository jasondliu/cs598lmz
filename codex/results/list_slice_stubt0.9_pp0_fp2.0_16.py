import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst[0]=A()
keepalive.append(lst[0])
lst[0].foo=weakref.ref(A(),callback)
del keepalive[0]
del keepalive[0]
lst=[]
keepalive=[]

import weakref
class C(object):pass
ob=C()
wr=[]
def callback(x):del wr[0]
ob.wr=wr
wr=[ob]
ob.wr[0].wr=weakref.proxy(ob,callback)
print ob.wr[0].wr
del ob

import weakref
l=[1,2,3]
def callback(x):del l[:]
wref=weakref.proxy(l,callback)
l.append(4)
print wref.append(4)
del l
try:print l
except NameError,err:print err
print wref

import weakref
class ExpensiveObject(object):
 def __del__(self):print 'deleting...'
obj=ExpensiveObject()
