import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst2=lst
print(a)
del a
print(lst2)
```

```
[In]
weakref.finalize()
```

```
[In]
lst=[str()]
a=A()
a.c=a
weakref.finalize(a,lambda x:del lst[0])
lst2=lst
print(a)
del a
print(lst)
```

```
[In]
lst=[str()]
a=A()
a.c=a
weakref.finalize(a,lambda x:del lst[0])
lst2=lst
print(a)
del a
print(lst)
```



### weakref.proxy 

> weakref.proxy 是一个类，可以生成弱引用（可以自动删除）的代理实例
