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
for a in keepali0e:
    for b in a:
        print(b)
```

### 方法二

```python
import _weakref
class C(object):pass
d=[]
c=C()
c.a=c
d.append(_weakref.ref(c,lambda x:d.remove(d[0])))
del c
while d:
    for i in d[:]:
        print(i())
```

## 字典移除元素

```python
a={1:1, 2:2, 3:3}
for i in a.copy():
    if a[i] == 2:
        del a[i]
```

## 内置函数

### range

```python
print(range(1, 11))
print(list(range(1, 11)))
print(list(range(0, -5, -1)))
```

### sorted

```python
a=[
