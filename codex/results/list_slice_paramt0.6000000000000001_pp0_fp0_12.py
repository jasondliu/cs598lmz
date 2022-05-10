import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print(lst)
a=None
print(lst)

import weakref
class A(object):pass
class B(object):pass
def callback(x):
    print("callback called")
    del lst[0]
keepalive=[]
lst=[]
a=A()
b=B()
a.c=b
b.c=a
lst.append(str())
keepalive.append(weakref.ref(a,callback))
print(lst)
del a,b
print(lst)

import weakref
class A(object):pass
a=A()
a.c=a
def callback(x):
    print("callback called")
    del lst[0]
lst=[]
lst.append(str())
keepalive=weakref.ref(a,callback)
print(lst)
del a
print(lst)

import weakref
class A(object):pass
a=A()
a.c=a
def callback(x):
    print("callback called
