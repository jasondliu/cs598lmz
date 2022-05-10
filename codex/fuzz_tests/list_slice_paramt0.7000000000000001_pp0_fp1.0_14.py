import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
keepali0e.append(weakref.ref(a.c))
keepali0e.append(weakref.ref(a.c,callback))
del a
del keepali0e
lst=[]
from weakref import WeakKeyDictionary
d=WeakKeyDictionary()
class A(object):pass
a=A()
d[a]=1
del a
try:d[A()]
except KeyError:pass
else:raise AssertionError
d={}
class A(object):pass
a=A()
d[a]=1
del a
d[A()]=1
import weakref
class A(object):pass
a=A()
b=A()
del A
r=weakref.ref(a)
r()is a
r=weakref.ref(b)
try:r()is b
except NameError:pass
else:raise AssertionError
class A(object):pass
a=A()
b=A()
del A
r=weakref.ref(a)
r()is a
r=weakref.
