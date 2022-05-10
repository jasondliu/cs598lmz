import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
b=A()
b.c=b
keepalive= [a,b]
del a,b
def f(a):a.c.c=lst
keepalive.append(callback)
del keepalive
a=A()
a.x=a
keepalive.append(a)
del keepalive,lst
a.x.x=callback
keepalive=[]
gcthread.start()
"""
"""
a=str()
def f():return a
keepalive=f
while 1:
    del keepalive
    a=str()
    keepalive=f
"""

"""
import gc
gc.set_debug(gc.DEBUG_SAVEALL | gc.DEBUG_UNCOLLECTABLE)
oldobjects = gc.garbage
def f():
    def g():
        pass
    g()
def h():
    pass
a.x=f
a.x()
del a,f,g,h
oldobjects = oldobjects[:]
print len(gc.garbage)
"""
"""
