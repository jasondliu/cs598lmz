import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst[0]+=chr(a)
```

### 例子2
```
class A(object):
    def __init__(self):
        self.x=None
    def __del__(self):
        print self.x
a=A()
a.x=a
del a
```

### 例子3

```
import weakref
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst[0]+=chr(a)
del a
```
### 例子4

```
import weakref
class A(object):
    def __init__(self,x):
        self.x=x
    def __del__(self):
        print self.x
keepali0e=[]
for x in xrange(0x100):
    a=A(x)
    keepali0e.append(weakref.ref(a,callback))

