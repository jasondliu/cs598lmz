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
#[str(), <weakref at 0x000002A9C8B8C948; to 'A' at 0x000002A9C8B8C898>]

#结论：
#当引用计数为0时，对象会被回收，但是在回收之前，会调用回调函数，回调函数中的参数是弱引用对象，
#因此在回调函数中，弱引用对象的引用计数为0，因此
