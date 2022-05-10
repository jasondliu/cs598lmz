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

```

```python

import weakref
a=A()
a.c=A()
a.c=A()
id(a)
a.b=A()
id(a.b)
id(a.c)
id(a.d)
a=A()
a.c=A()
a.c=A()
id(a)
a.b=A()
id(a.b)
id(a.c)
id(a.d)
if(True):global bb;bb=a;
sys.getrefcount(a)
del bb
sys.getrefcount(a)
a=A();import gc;gc.collect();
sys.getrefcount(A),sys.getrefcount(A())
import gc;del a;gc.collect()
del class_that_hangs_on_to_a
a=A.__new__(A)
import gc;gc.collect()
sys.getrefcount(A),sys.getrefcount(A())
sys.getrefcount(a)
