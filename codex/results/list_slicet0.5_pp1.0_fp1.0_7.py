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
print keepali0e
#import gc
#gc.collect()
#print gc.garbage

print "*"*50
import weakref
import gc
def callback(x):print x
class A(object):pass
a=A()
a.c=a
w=weakref.ref(a,callback)
del a
print gc.garbage
print w
print "*"*50
import weakref
import gc
def callback(x):print x
class A(object):pass
a=A()
a.c=a
w=weakref.ref(a,callback)
del a
print gc.garbage
print w
print "*"*50
import weakref
import gc
def callback(x):print x
class A(object):pass
a=A()
a.c=a
w=weakref.ref(a,callback)
del a
print gc.garbage
print w
print "*"*50
import weakref
import gc
def callback(x):print x
class A(object):pass

