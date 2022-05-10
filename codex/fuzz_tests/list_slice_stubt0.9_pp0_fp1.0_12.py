import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive=a
keepalive=lst[0]
a.c=None
lst[:1]=[]
print lst
c=callback
del lst
del keepalive,keepali0e
del a
del c
# memory error
class A(object):pass
def callback(x):pass
lst=[str()]
for i in xrange(100000):
    keepalive=weakref.ref(lst,callback)
    keepalive
# memory error
class File(object):pass
class A(object):
    def x(self):
        f=File()
# generic,memory error
import weakref
class A(object):pass
def callback(x,callback_lock):
    del callback_lock[0]
lst=[A()]
alock=[]
ar=weakref.ref(lst[0],lambda s:callback(s,alock))
ar
del lst
del alock
# function
def f():pass
f.__dict__[None]=f
del f
# function
def a():
   
