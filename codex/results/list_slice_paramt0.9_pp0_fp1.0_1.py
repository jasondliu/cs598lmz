import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a, callback))
del a
lst
```
* [weakref.ref(object[, callback])](https://docs.python.org/3/library/weakref.html#weakref.ref)
* [2.4.1. 弱引用](https://docs.python.org/3/library/weakref.html#module-weakref)

![](https://mmbiz.qpic.cn/mmbiz_png/gnfhCRqKqZlNsxtZia8lCYhYwibBQ2KrTzNCXicCkMibITRWicaZricfSSgKMLJGnHsEBsBiaF2jyE0X0cHhNITPicaoibg/0?wx_fmt=png)

## 5、单线程的Python
Python的GIL（Global Interpreter Lock）不会让多线程多核显卡加速爆发。
