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

# Test weakref.ref() with a callable that raises an exception
import sys,weakref
class A(object):pass
a=A()
def f(*args,**kw):1/0
w=weakref.ref(a,f)
del a
test_support.gc_collect()
w()

# Test weakref.ref() with a callable that raises an exception and an argument
import sys,weakref
class A(object):pass
a=A()
def f(*args,**kw):1/0
w=weakref.ref(a,f,42)
del a
test_support.gc_collect()
w()

# Test weakref.ref() with a callable that raises an exception and an argument
import sys,weakref
class A(object):pass
a=A()
def f(*args,**kw):1/0
w=weakref.ref(a,f,42,foo=42)
del a
test_support.gc_collect()
w()

# Test weakref.ref() with a callable that raises an exception and keyword
