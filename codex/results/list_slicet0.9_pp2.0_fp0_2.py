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
#解决2
import gc
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
def f():
    a=A()
    a.c=a
    keepali0e.append(weakref.ref(a,callback))
f()
del f
gc.collect()
while lst:keepali0e.append(lst[:])
#解决3
import gc
import weakref
class A(object):pass
count=0
def callback(x):
    global count
    count+=1
    del lst[0]
keepali0e=[]
lst=[str()]
def f():
    a=A()
    a.c=a
    keepali0e.append(weakref.ref(a,callback))
f()
del f
gc.collect()
while lst:
    keepali0e.append(lst[:])
assert count==1
