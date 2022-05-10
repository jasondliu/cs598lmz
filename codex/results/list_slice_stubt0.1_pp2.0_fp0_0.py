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
#[str(), <weakref at 0x000002A9E8E8D948; to 'A' at 0x000002A9E8E8D898>]
#[str()]

#结论：
#当一个对象的引用计数为0时，它会被垃圾回收器回收，但是如果它的引用计数不为0，它就不会被回收。
#当一个对象的引用计数为0时，它会被垃圾回收
