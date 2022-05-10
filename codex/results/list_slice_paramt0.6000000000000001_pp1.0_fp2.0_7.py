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
del a
del a
while lst:pass

#!/usr/bin/env python
import weakref
import gc
class A(object):pass
class B(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
b=B()
a.c=b
b.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(b,callback))
del a
del b
while lst:pass

#!/usr/bin/env python
import weakref
import gc
class A(object):pass
class B(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
b=B()
a.c=b
b.c=a
keepali0e.append(weakref.
