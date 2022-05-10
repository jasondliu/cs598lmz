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
#[str(), <weakref at 0x000001F8D9B9B948; to 'A' at 0x000001F8D9B9B898>]
#[<__main__.A object at 0x000001F8D9B9B898>]

#结论：
#当一个对象的引用计数为0时，它会被垃圾回收器回收，但是如果它有弱引用，那么它就不会被回收，
#因为弱引用不会增加对
