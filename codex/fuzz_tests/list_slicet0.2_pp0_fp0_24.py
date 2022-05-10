import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
print(keepali0e)

#练习3
import weakref
class A(object):pass
def callback(x):print(x)
a=A()
a.c=a
keepali0e=weakref.ref(a,callback)
del a

#练习4
import weakref
class A(object):pass
def callback(x):print(x)
a=A()
a.c=a
keepali0e=weakref.ref(a,callback)
del a

#练习5
import weakref
class A(object):pass
def callback(x):print(x)
a=A()
a.c=a
keepali0e=weakref.ref(a,callback)
del a

#练习6
import weakref
class A(object):pass
def callback(x):print(x)
a=A()
a.c=a
keepali0e=weakref.ref(a,callback)
del a

#练习7
import
