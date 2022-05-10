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
#[str(), <weakref at 0x000002A9D9E8C8C8; to 'A' at 0x000002A9D9E8C7B8>]

#结论：
#当一个对象的引用计数为0时，它会被垃圾回收器回收，但是如果它有循环引用，
#那么它的引用计数永远不会为0，也就永远不会被回收。
#所以，如果一个对
