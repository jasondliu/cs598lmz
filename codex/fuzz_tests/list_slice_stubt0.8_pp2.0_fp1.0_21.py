import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
keepali0e.append(weakref.ref(lst,callback))
import gc
gc.collect()
print len(lst)
[w() for w in keepali0e]
print len(lst)

def f():return g()
def g():return [lst]
h=f
keepali0e=[weakref.ref(lst,callback),h]
def g():return weakref.ref(lst,callback)
#h=f
keepali0e.append(h())
del h
print len(lst)
[w() for w in keepali0e]
print len(lst)

def f():"docstring"
print f.__doc__
def f():pass
print f.func_doc

def f(a,b,c):pass
print f.func_code.co_nlocals
print f.func_code.co_nloc
