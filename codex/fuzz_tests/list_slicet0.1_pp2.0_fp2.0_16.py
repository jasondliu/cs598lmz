import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
print(keepali0e)

#结果：
#[<weakref at 0x000002A8B9A8D948; to 'A' at 0x000002A8B9A8D908>, ['']]
#[<weakref at 0x000002A8B9A8D948; dead>, ['']]
#[<weakref at 0x000002A8B9A8D948; dead>, []]

#结论：
#1.当对象被回收时，weakref.ref()对象会被自动回收，并且调用回调函数
#2.当对象被回收时，weakref.ref()对象会被自动回收，但是不会
