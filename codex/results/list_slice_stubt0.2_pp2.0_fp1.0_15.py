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
#[str(), <weakref at 0x0000020A9D9F7E08; to 'A' at 0x0000020A9D9F7D68>]
#[str()]

#结论：
#当对象被回收时，会调用回调函数，并且会将对象从列表中删除。

#问题：
#1.为什么会调用回调函数？
#2.为什么会将对象从列表中删除？
#3.为什么会
