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
#[str(), <weakref at 0x000002A8B9E0D948; to 'A' at 0x000002A8B9E0D898>]

#结论：
#当一个对象的引用计数为0时，它会被垃圾回收，但是如果它有弱引用，那么它会被延迟回收，直到所有的弱引用都被回收。
#当一个对象的引用计数为0时，它会
