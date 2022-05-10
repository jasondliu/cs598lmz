import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
def getkeepali0e():return keepali0e[0]()
del lst[0]
del keepali0e
del a
lst=None
import sys
print sys.getrefcount(getkeepali0e())
def getCircularRef():return getkeepali0e()
print sys.getrefcount(getkeepali0e())
print sys.getrefcount(getCircularRef())

#OutPut


import ctypes
import _ctypes
import gc
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
def getkeepali0e():return keepali0e[0]()
del lst[0]
del keepali0e
del a
lst=None
import sys
print sys.getrefcount(getkeepali0e())

gc.collect()
print sys.getref
