import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
print(lst)
del a.c
print(lst)
del a
print(lst)

"""

"""
import weakref
class A(object):pass
def callback(x):print('callback is called')
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
print(lst)
del a.c
print(lst)
del a
print(lst)

"""

"""
import weakref
class A(object):pass
def callback(x):print('callback is called')
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
print(lst)
del a.c
print(lst)
del a
print(lst)

"""

"""
import weakref
class A(object):pass
def callback(x):print('
