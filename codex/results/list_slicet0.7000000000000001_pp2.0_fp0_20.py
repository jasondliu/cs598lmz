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
len_=len(keepali0e)-1
keepalive=[None]*len_
for i in range(len_):keepalive[i]=keepali0e[i+1]
keepalive=keepalive[0]
print('{} keepalive objects are kept alive'.format(len(keepalive)))
```

```python
import weakref
class A(object):pass
def callback(x):print('callback')
keepalive=[]
a=A()
a.c=a
keepalive.append(weakref.ref(a,callback))
del a
print('the object is deleted')
while keepalive:keepalive.pop()
print('the cyclic reference is deleted')
```

The problem is that `weakref.ref` has registered a `callback` function for
the object. When the object is deleted, the `callback` function is called.
The `callback` function needs to access the object itself.
As a result, a cyclic reference is automatically created.
The object will not be garbage collected.

The solution is to
