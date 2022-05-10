import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst

#output:
#['<__main__.A object at 0x7f5e5c5f7e10>']

#explanation:
#the weakref callback is not called because the object is still reachable through the cycle.
#the cycle is not broken until the last reference to the object is removed.

#example 2:
#the cycle is broken when the last reference to the object is removed.
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
del keepali0e
print lst

#output:
#[]

#example 3:
#the cycle is broken when the last reference to the object is removed.
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a
