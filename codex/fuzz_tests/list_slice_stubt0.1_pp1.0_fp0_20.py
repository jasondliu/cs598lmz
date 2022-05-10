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
#[str(), <weakref at 0x000002A5D5F6E948; to 'A' at 0x000002A5D5F6E898>]
#[str(), None]

#结论：
#当弱引用对象被回收时，会调用回调函数，并将弱引用对象从列表中删除。
#当弱引用对象被回收时，会调用回调函数，并将弱引用对象从列表中删除。

