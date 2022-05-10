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
#[str(), <weakref at 0x000002A9B9C9E948; to 'A' at 0x000002A9B9C9E948>]
#[<__main__.A object at 0x000002A9B9C9E948>]

#结论：
#当弱引用对象被回收时，会调用回调函数，回调函数的参数是弱引用对象本身，而不是被弱引用的对象。
#回调函数的参数是弱引用
