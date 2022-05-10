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
#[str(), <weakref at 0x000002A9E9F9C948; to 'A' at 0x000002A9E9F9C828>]

#结论：
#当弱引用对象被回收时，会调用回调函数，回调函数的参数是弱引用对象，而不是被引用的对象。
#回调函数的参数是弱引用对象，而不是被引用的对象。

#结论：

