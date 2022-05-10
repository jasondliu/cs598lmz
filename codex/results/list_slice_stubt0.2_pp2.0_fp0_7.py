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
#[str(), <weakref at 0x000002B9D9A9C948; to 'A' at 0x000002B9D9A9C948>]

#结论：
#当弱引用指向的对象被回收时，回调函数会被调用，并且弱引用对象会被自动删除。
#回调函数的参数是弱引用对象本身，而不是被引用的对象。
#回调函数在对
