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
#[str(), <weakref at 0x000002A8D9E8A948; to 'A' at 0x000002A8D9E8A898>]

#结论：
#当弱引用对象被回收时，会调用回调函数，回调函数可以接收一个参数，这个参数就是被回收的弱引用对象。
#回调函数可以是任意的可调用对象，比如函数、方
