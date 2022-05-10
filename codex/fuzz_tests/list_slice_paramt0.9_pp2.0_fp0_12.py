import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
if not __debug__:del a.c
a1=A()
a2=A()
a2.a3==a3
del a3
del a2
a1.a3==a3
class B(object):pass
b1=B()
b2=B()
b2.b3==b3
del b2
del b1
a1.a3==a3
del a1
del b3
del a3
def foo():pass
def callback(x):del lst[0]
lst=[]
def resolver(lst):lst.append(str())
o=weakref.ref(object(),callback,resolver)
del o
lst[0]
try:del o
except ReferenceError:pass
else:raise TestFailed
if not __debug__:del o
lst=[]
def resolver(lst):
    lst.append(str())
    raise RuntimeError
o=weakref.ref(object(),callback,resolver)
del o
lst[0]
import sys

