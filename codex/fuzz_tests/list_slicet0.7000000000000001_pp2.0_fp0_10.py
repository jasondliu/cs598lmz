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

#代码块3
import gc,weakref,sys
class A(object):pass
lst=[]
def callback(x):del lst[0]
def f():
    a=A()
    a.c=a
    lst.append(weakref.ref(a,callback))
    del a
f()
gc.collect()
print(sys.getrefcount(lst))
del lst
while gc.collect():pass

#代码块4
import gc,weakref,sys
class A(object):pass
lst=[]
def callback(x):del lst[0]
def f():
    a=A()
    a.c=a
    lst.append(weakref.ref(a,callback))
    del a
f()
gc.collect()
print(sys.getrefcount(lst))
del lst
while gc.collect():pass

#代码块5
class A(object):pass
del A

#代码
