import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
a.a=a
keepalive.append(a)
lst.append(a)
keepalive.append(lst)
weakref.ref(lst,callback)
del keepalive,lst,a
gc.collect()
```

这里的`keepalive`是一个list，里面存放了两个对象，第一个是`a`，第二个是`lst`。

`lst`是一个list，里面存放了两个对象，第一个是`str()`，第二个是`a`。

`a`是一个`A`类的实例，有三个属性，分别是`a`、`b`、`c`
