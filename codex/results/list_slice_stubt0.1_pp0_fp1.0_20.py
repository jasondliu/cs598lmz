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
#[str(), <weakref at 0x000002A1E8B8B948; to 'A' at 0x000002A1E8B8B898>]
#[str()]

#结论：
#当弱引用的对象被回收时，会调用回调函数，并将弱引用对象从列表中删除。

#练习：
#1.编写一个程序，让它创建一个WeakValueDictionary，并将字符串作为键，数字作
