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
```

```python
with open("flag","r")as f:print f.read()
```
解决方法就是保证`lst`的长度不能小于`len(keepali0e)`（`lst`的内存一定在`keepali0e`的后面）

```python
with open("flag","r")as f:print f.read()
# 而lst的内存一定在keepali0e的后面
lst=['\x00']*(len(keepali0e)+1)#就可以保证lst的内存在keepali0e的后面
```

我们尝试运行一下，发现`with`报错了

![1540403844090](https://i.loli
