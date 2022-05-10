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
#weakref.ref.__init__()
"""
"""
import weakref
class A(object):pass
def callback(x):del lst[0]
lst=[str()]
a=A()
a.c=a
wr=weakref.ref(a,callback)
del a
print lst
wr()
"""
"""
import weakref
class A(object):pass
def callback(x):del lst[0]
lst=[str()]
a=A()
a.c=a
wr=weakref.ref(a,callback)
del a
print lst
wr()
"""
"""
import weakref
class A(object):pass
def callback(x):del lst[0]
lst=[str()]
a=A()
a.c=a
wr=weakref.ref(a,callback)
del a
print lst
wr()
"""
"""
import weakref
class A(object):pass
def callback(x):del lst[0]
lst=[str
