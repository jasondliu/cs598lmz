import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst[0]=""
print(lst[0])
del a
del keepali0e
import gc
gc.collect()
print(lst[0])
print(lst[0][0])
"""

"""
import weakref
class A(object):pass
def callback(x):print("callback")
lst=[]
a=A()
a.c=a
lst.append(weakref.ref(a,callback))
del a
print(lst[0]())
"""
"""
import weakref
class A(object):pass
def callback(x):print("callback")
lst=[]
a=A()
a.c=a
lst.append(weakref.ref(a,callback))
del a
print(lst[0]().c())
"""
"""
class MyClass:
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return "MyClass:name=%s"%self.name
my_obj=MyClass("
