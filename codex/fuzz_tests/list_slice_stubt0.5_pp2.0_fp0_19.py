import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
b=A()
b.c=b
lst.append(a)
lst.append(b)
keepalive=[]
keepalive.append(a)
keepalive.append(b)
del a
del b
lst[0]=keepalive[0]
lst[1]=keepalive[1]
del keepalive
lst[0].c=lst[1]
lst[1].c=lst[0]
lst.append(weakref.ref(lst[0],callback))
lst.append(weakref.ref(lst[1],callback))
del lst[0]
del lst[0]
del lst[0]
del lst[0]
del lst
```

As we can see, the `del lst[0]` and `del lst[1]` in the callback function will not be executed.

The reason is that the `reference` in `weakref` is implemented as a `dict`.

```python
>>> import weakref
>>> weakref.Reference
