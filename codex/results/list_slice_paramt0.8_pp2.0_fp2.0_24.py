import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(lst,callback))
del a
del keepali0e
print(lst)
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
keepali0e.append(weakref.ref(lst,callback))
a.c=a
del a
del keepali0e
print(lst)
class A(object):pass
a=A()
b=A()
a.c=b
b.c=a
del a
del b
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
keepali0e.append(weakref.ref(lst,callback))
b=A()
a.c=b
b.c=a
del a
del b
del keepali0e
print(lst)
class A(object):pass
def callback(x):del lst[0]
keepali0e
