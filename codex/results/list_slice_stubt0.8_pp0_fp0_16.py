import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
for i in range(10):
    c=A()
    c.name=i
    lst.append(c)
    weakref.ref(c,callback)
    del c
    print len(lst)
```

### 使用getattr访问属性其实引用很多内置函数

```python
a = 3
b = getattr(__builtins__,'_'+str(3))
print b

a = 3.0
b = getattr(__builtins__,'_'+str(3))
print b

a = '3'
b = getattr(__builtins__,'_'+str(3))
print b

a = 3L
b = getattr(__builtins__,'_'+str(3))
print b
```

### 打印所有python内置函数

```python
import sys

