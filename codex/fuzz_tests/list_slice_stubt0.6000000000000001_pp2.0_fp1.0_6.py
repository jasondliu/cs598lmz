import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
b=A()
b.c=a
a.b=b
lst.append(a)
lst.append(b)
lst.append(a)
lst.append(b)
del a,b
lst[1]=weakref.ref(lst[1],callback)
lst[3]=weakref.ref(lst[3],callback)
keepalive.append(lst)
len(lst)

from __future__ import print_function
from pprint import pprint
import gc
import weakref
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.c=a
b=A()
b.c=a
a.b=b
lst.append(a)
lst.append(b)
lst.append(a)
lst.append(b)
del a,b
lst[1]=weakref.ref(lst[1],callback)
lst[3]=weakref.
