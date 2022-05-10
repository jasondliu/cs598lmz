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
#[str(), <weakref at 0x000002A9B7E8B948; to 'A' at 0x000002A9B7E8B898>]

#结论：
#当对象被删除时，弱引用会被自动删除，并且调用回调函数

#问题：
#1.为什么弱引用会被自动删除？
#2.为什么弱引用会调用回调函数？
#3.为什么弱
