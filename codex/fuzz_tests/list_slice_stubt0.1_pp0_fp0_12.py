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
print(keepalive)

#结果：
#[str(), <weakref at 0x000002A8F8B9B948; to 'A' at 0x000002A8F8B9B908>]
#[<__main__.A object at 0x000002A8F8B9B908>]

#结论：
#当一个对象的引用计数为0时，它会被回收，但是如果它有弱引用，那么它会被放入垃圾回收器的待回收队列中，
# 当垃圾
