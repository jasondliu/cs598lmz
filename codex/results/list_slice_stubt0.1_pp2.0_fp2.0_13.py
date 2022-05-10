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
#[str(), <weakref at 0x000002B8E9F9B848; to 'A' at 0x000002B8E9F9B7F0>]

#结论：
#当一个对象的引用计数为0时，它会被回收，但是如果它的引用计数为0，但是它的弱引用计数不为0，那么它不会被回收。
#当一个对象的弱引用计数为0时，它会被回
