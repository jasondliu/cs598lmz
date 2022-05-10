import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
callback=functools.partial(callback,a)
weakref.ref(lst[0],callback)
del keepalive
del lst
del a
del callback
gc.collect()
```

```
python -X tracemalloc -c "lst=[1,2,3];lst[0]=str()"
```
