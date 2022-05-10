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
#[str(), <weakref at 0x000002A8D9E9A948; to 'A' at 0x000002A8D9E9A898>]

#结论：
#当对象被回收时，会调用回调函数，并且回调函数的参数是被回收的对象
#回调函数的参数是被回收的对象，而不是弱引用对象
#回调函数的参数是被回收的对象
