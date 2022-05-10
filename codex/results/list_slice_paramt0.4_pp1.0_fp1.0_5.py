import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
del a
del lst
gc.collect()
print(keepali0e[0]())

#3.4.4.3
import weakref
class A(object):pass
def callback(x):print("callback")
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
del a
del lst
gc.collect()
print(keepali0e[0]())

#3.4.4.4
import weakref
class A(object):pass
def callback(x):print("callback")
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
del a
del lst
gc.collect()
print(keepali0e[0]())

#3.4.4.5
import
