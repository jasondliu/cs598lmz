import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
del a
print(lst)

#结果：
#[str(), <weakref at 0x000002A6C9E6B948; to 'A' at 0x000002A6C9E6B898>]

#结论：
#当弱引用的对象被回收时，调用回调函数，并且删除弱引用对象。

#问题：
#1.为什么要用弱引用？
#2.为什么要用回调函数？
#3.为什么要用弱引用对象？

