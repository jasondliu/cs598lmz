import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
b=A()
b.c=b
keepali0e.append(weakref.ref(b,callback))
a=None
b=None
del keepali0e[:]
del lst
gc.collect()

import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
a=None
gc.collect()
"""

#test__fsref_to_pyref:
"""
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
a=None
gc.collect()
"""

#test__fsref_to_pyref2:
"""
import weakref
class A(object):pass
def callback
