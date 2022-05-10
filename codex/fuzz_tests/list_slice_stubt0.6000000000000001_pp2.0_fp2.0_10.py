import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive=a
keepalive.c=lst
keepalive.d=callback
lst[0]=keepalive
```

```
import gc
import weakref
class A(object):pass
def callback(x):del lst[0]
keepalive=[str()]
lst=[A()]
lst[0].c=lst
lst[0].d=callback
lst[0].c=keepalive
```

```
import gc
import weakref
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[A()]
lst[0].c=lst
lst[0].d=callback
lst[0].c=keepalive
```

```
import gc
import weakref
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[A()]
lst[0].c=lst
lst[0].d=callback

