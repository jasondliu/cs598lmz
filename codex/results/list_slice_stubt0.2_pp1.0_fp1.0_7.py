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
#[str(), <weakref at 0x000002A2E9C9E948; to 'A' at 0x000002A2E9C9E898>]
#[str()]

#结论：
#当一个对象的弱引用被回调函数删除后，该对象的引用计数为0，该对象会被垃圾回收机制回收。
#当一个对象的弱引用被回调函数删除后，该对象的引用
