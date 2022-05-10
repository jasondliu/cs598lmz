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

```
Python3的例子
>>> import weakref
>>> def callback(x):
...   del lst[0]
...
>>> keepalive = []
>>> lst = [str()]
>>> a = A()
>>> a.c = a
>>> keepalive.append(weakref.ref(a, callback))
>>> del a
>>> while lst:
...   keepalive.append(lst[:])
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
RuntimeError: maximum recursion depth exceeded while calling a Python object
>>>
```



# 读入一个无限循环的文件

```
while True:
    line = input()
    if line == '42':
        break
    print(line)

```


# 读入一个无限循环的文件，做奇怪的
