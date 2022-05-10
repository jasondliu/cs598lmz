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
#[str(), <weakref at 0x000002A8C9D9E948; to 'A' at 0x000002A8C9D9E898>]

#结论：
#当一个对象的引用计数为0时，它会被回收，但是如果它的弱引用计数不为0，它就不会被回收，
#因为它的弱引用计数不为0，所以它的弱引用不会被回收，所以它的弱
