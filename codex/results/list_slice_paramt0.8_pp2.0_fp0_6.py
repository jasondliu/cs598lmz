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
print(lst)
#[]


import gc
import weakref
class A(object):pass
def callback(x):print('deleted')
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
a=None
gc.collect()
lst[0]=None
gc.collect()
print(lst)
#['', ]

import weakref
class A(object):pass
def callback(x):print('deleted')
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
a=None
lst[0]=None
del lst[0]
print(lst)
#[]

import weakref
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
