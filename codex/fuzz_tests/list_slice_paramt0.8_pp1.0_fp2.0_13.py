import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(str())
del a
while keepali0e:pass
import gc
gc.collect()
print len(lst)
def f():pass
def g(h):return h()()
print g(f)
def g(h):return h()
def h():return 1
print g(h)
def g():return h()
def h():return 1
print g()
def g():return h()
def h():return 1
print g()
def g(h):return h()
def h():return 1
print g(h)
def g(f,i=f):return i()
def f():return h
def h():return 1
print g(f)
def f(g):return g(0)
def g(a):return a
print f(g)
def f(g):return g(0)
def g(a):return a
print f(g)
def f(g):return g(0)
def g(a):return a
print f(g)
def f(g):return g(0)
def
