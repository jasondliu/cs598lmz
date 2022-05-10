import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
w=weakref.ref(a,callback)
del a
del lst
import gc
gc.collect()
print(w())
"""

"""
import weakref
class A(object):
    def __init__(self,name):
        self.name=name
    def __del__(self):
        print(self.name)
a=A('a')
b=A('b')
w=weakref.ref(a)
print(w)
print(w())
print(w() is a)
print(w() is b)
del a
print(w())
print(w() is b)
"""

"""
import weakref
class A(object):
    def __init__(self,name):
        self.name=name
    def __del__(self):
        print(self.name)
a=A('a')
b=A('b')
c=A('c')
d=A('d')
e=A('e')
w=weak
