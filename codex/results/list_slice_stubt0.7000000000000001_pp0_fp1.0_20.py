import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalie.append(a)
lst[0]='\x00'*16
lst.append(weakref.ref(a,callback))
print lst
# del a
# del keepalie[0]
# print lst
# Output: ...
# RuntimeError: deallocated C object
# This shows that the C object has been deleted,
# but the callback function cannot be called because of the loop.
```

```python
import weakref
class A(object):pass
lst=[str()]
a=A()
a.c=a
keepalie.append(a)
lst[0]='\x00'*16
lst.append(weakref.ref(a))
del a
del keepali0e[0]
print lst
# Output: ...
# RuntimeError: deallocated C object
# This shows that the C object has been deleted,
# but the callback function cannot be called because of the loop.
```

```python
import weakref
class A(object):pass
def callback(x):del
