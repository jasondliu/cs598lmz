import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(weakref.ref(a,callback))
lst.append(weakref.ref(str(),callback))
lst.append(weakref.ref(a,callback))
keepalive.append(lst)
for i in range(10000):
    pass
import gc
gc.collect()
print(len(lst))

"""
"""
import gc
class A(object):
    pass
def callback(x):
    del lst[0]
keepalive=[]
lst=[str()]
a=A()
lst.append(weakref.ref(a,callback))
lst.append(weakref.ref(str(),callback))
lst.append(weakref.ref(a,callback))
keepalive.append(lst)
for i in range(1000):
    pass
gc.collect()
print(len(lst))
"""
"""
import gc
class A(object):
    pass
def callback(x):
    del lst[0]
keepalive=[]
lst=[str()
