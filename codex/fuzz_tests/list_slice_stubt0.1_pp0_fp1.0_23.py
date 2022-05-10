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
#[str(), <weakref at 0x000002A9F7C9B948; to 'A' at 0x000002A9F7C9B948>]

#结论：
#当一个对象的引用计数为0时，它就会被垃圾回收器回收，但是如果它的引用计数不为0，
#那么它就不会被回收，即使它的引用计数不为0，但是它的引用计数为0，
