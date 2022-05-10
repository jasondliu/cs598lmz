import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst
"""
#print a.c
"""
import weakref
class A(object):pass
lst=[]
a=A()
a.c=a
lst.append(weakref.ref(a))
del a
print lst[0]()
print lst[0]()
"""
"""
import weakref
class A(object):pass
lst=[]
a=A()
a.c=a
lst.append(weakref.ref(a))
del a
print lst
print lst[0]()
"""
"""
import weakref
class A(object):pass
lst=[]
a=A()
a.c=a
lst.append(weakref.ref(a))
del a
print lst[0]()
print lst[0]()
"""
"""
import weakref
class A(object):pass
lst=[]
a=A()
a.c=a
lst.append(weakref.ref(a))
del a
print lst
print
