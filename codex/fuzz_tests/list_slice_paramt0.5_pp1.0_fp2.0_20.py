import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
print(lst)
del a
print(lst)
a=A()
keepali0e.append(weakref.ref(a,callback))
print(lst)
del a
print(lst)
print(keepali0e)

print('---------------------------------------------------------')

import sys,gc
a=A()
a.c=a
keepali0e=weakref.ref(a)
print(sys.getrefcount(a))
del a
print(sys.getrefcount(keepali0e()))
print(keepali0e())
gc.collect()
print(keepali0e())

print('---------------------------------------------------------')

import gc
class A(object):
    def __init__(self):
        self.lst=[]
    def add(self,obj):
        self.lst.append(obj)
    def __del__(self):
        print('A.__del__')
        del self.lst

a=
