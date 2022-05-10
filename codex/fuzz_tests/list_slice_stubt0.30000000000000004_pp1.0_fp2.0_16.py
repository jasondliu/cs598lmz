import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a.x=weakref.ref(lst,callback)
print(lst)

#2.1.2.2
import weakref,gc
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a.x=weakref.ref(lst,callback)
print(lst)
del a
gc.collect()
print(lst)

#2.1.2.3
import weakref,gc
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a.x=weakref.ref(lst,callback)
print(lst)
del a
del keepalive
gc.collect()
print(lst)

#2.1.2.4
import weakref
