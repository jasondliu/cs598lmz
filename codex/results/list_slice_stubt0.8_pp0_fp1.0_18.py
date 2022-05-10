import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=a.c
a.e=a.d
a.f=a.e
a.g=a.f
a.h=a.g
a.i=a.h
a.j=a.i
weakref.ref(a,callback)
del a
gc.collect()

```


```python

class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.c=a
a.d=a.c
a.e=a.d
a.f=a.e
a.g=a.f
a.h=a.g
a.i=a.h
a.j=a.i
weakref.ref(a,callback)
del a
lst
gc.collect()
lst

```

## 8.类的创建和使用对对象的引用次数的影响

