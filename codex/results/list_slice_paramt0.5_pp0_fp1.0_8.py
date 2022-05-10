import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst[0]='a'
print(a)
del a
print(lst)

#6.3.3
import weakref
class A(object):pass
def callback(x):del lst[0]
lst=[str()]
a=A()
a.c=a
lst[0]=a
print(a)
del a
print(lst)

#6.3.4
import weakref
class A(object):pass
def callback(x):del lst[0]
lst=[str()]
a=A()
a.c=a
lst[0]=a
print(a)
del a
print(lst)

#6.4.1
import weakref
class A(object):pass
def callback(x):del lst[0]
lst=[str()]
a=A()
a.c=a
lst[0]=a
print(a)
del a
print(lst)

#6.4.2
import weakref
class A(object):
