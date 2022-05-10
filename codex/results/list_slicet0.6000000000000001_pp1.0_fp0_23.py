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

### 说明

```
Python 的对象分为四种类型：

常量（Numbers, Strings, Tuples）：编译时分配内存。
普通对象（Objects）：创建时分配内存。
弱引用对象（Weakref）：创建时分配内存。
自定义对象（User Defined）：创建时分配内存。

Python 中的引用计数机制会跟踪每一个对象的引用数量，当
