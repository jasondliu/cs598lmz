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
#[str(), <weakref at 0x000002B9D9A8A8C8; to 'A' at 0x000002B9D9A8A898>]
#[<__main__.A object at 0x000002B9D9A8A898>]

#结论：
#当弱引用的对象被回收时，会调用回调函数，回调函数的参数是弱引用对象的引用，
# 回调函数的返回值会被忽略，回调函数
