import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.callback=callback
keepali0e.append(a)
keepali0e.append(lst)
del lst
print lst[0]
```

# 反射访问

## 访问被`__slots__ = ('bb','cc')`限制的属性

python内置函数dir()，可以返回对象的属性列表，但是它无法返回动态添加的属性，也不能返回类属性。

除了dir()，python还提供了一个特殊的内置函数，叫做getattr()。

getattr(object, name, [default])

该函数使
