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
#[<weakref at 0x000002A8A9A7D948; to 'A' at 0x000002A8A9A7D908>, ['']]
#[<weakref at 0x000002A8A9A7D948; dead>, ['']]
#[<weakref at 0x000002A8A9A7D948; dead>, []]
#[]

#结论：
#1.当对象被回收时，weakref.ref对象的callback函数会被调用，并且weakref.ref对象会变成dead状态
#2.当对象被回收时，weakref.ref对象的callback函数会被调用
