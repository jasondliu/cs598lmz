import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
del a,lst
import gc
print gc.collect()
"""
"""
class A(object):pass
def callback(x):print 'callback'
lst=[]
a=A()
a.c=a
lst.append(weakref.ref(a.c,callback))
del a
import gc
print gc.collect()
"""
"""
import weakref
class A(object):pass
def callback(x):print 'callback'
lst=[]
a=A()
a.c=a
lst.append(weakref.ref(a.c,callback))
del a
import gc
print gc.collect()
"""

"""
import weakref
class A(object):pass
def callback(x):print 'callback'
lst=[]
a=A()
a.c=a
lst.append(weakref.ref(a.c,callback))
del a
import gc
print gc.collect()
"""

"""
def func():
    def bar():
        return "f
