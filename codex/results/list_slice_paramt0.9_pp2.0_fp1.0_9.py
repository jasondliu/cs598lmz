import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst[0].startswith.func_code.co_flags=0xc
#print str()#提示前边用了gtk库
lst[0].startswith.func_code.co_flags=0x8
a.b=0x500000005
print chr(a.b)
```

这道题比较影响我的e8题，当时我后边的思路也就继续往下走了，没看到下边的绕过，要不然也就不会那么纠结了。

```python
import sys
class B(set):pass
class A(object):
    def __init__(self,val=0x1234):self.val=val
    def __re
