import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(a.c)
keepali0e.append(lst)
del a
del keepali0e
gc.collect()
lst[0]="x"*16
lst.append(lst)
lst.append(weakref.ref(lst,callback))
del lst
gc.collect()
```

首先，对象a与对象a.c构成了循环引用，因此在程序结束时不会被回收。当程序结束时，列表lst中只有一个元素，即字符串对象“\0”*16。

当我们在列表lst末尾添
