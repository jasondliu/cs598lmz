import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
print lst

#['']

#2
import weakref
class A(object):pass
def callback(x):del lst[0]
lst=[str()]
a=A()
a.c=a
keepali0e=weakref.ref(a,callback)
keepali0e=weakref.ref(a.c,callback)
del a
print lst

#['']

#3
import weakref
class A(object):pass
def callback(x):del lst[0]
lst=[str()]
a=A()
a.c=a
keepali0e=weakref.ref(a,callback)
keepali0e=weakref.ref(a.c,callback)
del a
print lst

#[]

#4
import weakref
class A(object):pass
def callback(x):del lst[0]
lst=[str()]
a=A()
a
