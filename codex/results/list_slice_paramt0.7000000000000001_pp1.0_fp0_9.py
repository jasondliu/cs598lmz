import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a))
a.c=None
del a
import gc
gc.collect()
print len(keepali0e)
print lst,len(lst)
if len(lst)==1:
  print lst[0]
def f():
  a=str()
  b=str()
  print a,b
f()
'''
'''
import weakref
class Graphic(object):pass
class Rectangle(Graphic):pass
lst=[]
a=Rectangle()
lst.append(weakref.ref(a))
print lst[0]()
del a
print lst[0]()
import gc
gc.collect()
print lst[0]()
'''
'''
import weakref
class Graphic(object):pass
class Rectangle(Graphic):pass
lst=[]
a=Rectangle()
lst.append(weakref.ref(a))
a.c=a
lst.append(weakref.ref(a))

