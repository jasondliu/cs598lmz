import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
lst[0]=weakref.ref(a,callback)
print(lst)

#结果：
#[<weakref at 0x0000000003C3D988; to 'A' at 0x0000000003C3D908>]

#结论：
#当弱引用的对象被回收时，回调函数会被调用，并且弱引用对象会被自动删除
#当弱引用对象被删除时，回调函数不会被调用

#问题：
#1.为什么弱引用对象被
