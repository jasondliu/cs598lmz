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
del keepali0e
from gc import collect
collect()
lst[0]()

from _weakref import ref
from gc import collect
from sys import getrefcount

def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
class A(object): pass
a=A()
a.c=a
keepali0e.append(ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
del keepali0e
from gc import collect
collect()
lst[0]()

from _weakref import ref
from gc import collect
from sys import getrefcount
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
class A(object): pass
a=A()
a.c=a
keepali0e.append(ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
del keepali0e
from gc import collect
