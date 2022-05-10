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
print keepali0e
```
<hr>
输出：
```
[[<weakref at 0x2aebc10; dead>, []]]
```

[返回目录](#目录)
## 参考

- [Python Weak Reference](https://www.ibm.com/developerworks/cn/linux/l-cn-weakref/)
- [Python基础教程](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)

[返回目录](#目录)
