import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append((a,lst))
wref=weakref.ref(a,callback)
print(wref)
del a
print(lst)
print('-----------------')

import weakref
class A(object):pass
def callback(x):del lst[0]
lst=[str()]
a=A()
wref=weakref.ref(a,callback)
print(wref)
del a
print(lst)
