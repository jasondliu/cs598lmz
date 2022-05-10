import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
#a.a=a
keepalive=(a,keepali0e)
callback=weakref.ref(a,callback)
keepalive.append(callback)
keepalive.append(a.a)
del keepalive, keepali0e
lst.extend(range(1000000))
"""
import sys, gc

#if __debug__:
#    gc.set_debug(gc.DEBUG_STATS)

def foo():
    return int()

def bar():
    return foo()

def baz():
    return foo()

def f1():
    return sys.getrefcount(9)

def f2():
    return sys.getrefcount(9)

def g1():
    return sys.getrefcount(9)

def g2():
    return sys.getrefcount(9)

def h1():
    return sys.getrefcount(9)

def h2():
    return sys.getrefcount(9)

def f():
    for i in
