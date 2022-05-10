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

下面就用`keepal0ie`的例子来说明引用循环的问题。


```
In [1]: import gc

In [2]: keepal0ie=[]

In [3]: lst=[str()]

In [4]: a=A()

In [5]: a.c=a

In [6]: keepal0ie.append(weakref.ref(a,callback))

In [7]: del a

In [8]: while lst:keepal0ie.append(lst[:])
---------------------------------------------------------------------------
MemoryError                               Traceback (most recent call last)
<ipython-input-8-67269e0d182b> in <module>()
----> 1 while lst:keepal0ie.append(lst[:])

MemoryError: 

In [9]: keepal0ie
Out[9]: 
[<weakref at 0x0000002BC1D23418; dead>,

