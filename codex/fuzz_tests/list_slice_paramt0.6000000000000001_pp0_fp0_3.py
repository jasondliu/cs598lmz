import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
del keepali0e[0]
print lst
print "*"*50
import weakref
class A(object):pass
a=A()
a.c=a
lst=[a]
del a
print lst
print "*"*50
import weakref
class A(object):pass
a=A()
a.c=a
lst=[a]
lst[0]=str()
del a
print lst
print "*"*50
import weakref
class A(object):pass
a=A()
a.c=a
def callback(x):lst[0]=str()
keepali0e=[]
keepali0e.append(weakref.ref(a,callback))
del a
del keepali0e[0]
print lst
print "*"*50
import weakref
class A(object):pass
a=A()
a.c=a
def callback(x):lst[0]=str()
keepali0e=[]
keepali0e.append(weakref.ref
