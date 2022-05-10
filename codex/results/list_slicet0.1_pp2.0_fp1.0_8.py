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
#[<weakref at 0x000002A9B8B8A948; to 'A' at 0x000002A9B8B8A908>, ['']]
#[<weakref at 0x000002A9B8B8A948; dead>, ['']]
#[<weakref at 0x000002A9B8B8A948; dead>, []]
#[]

#结论：
#1.当对象被回收时，weakref.ref()对象会自动被回收，并且会调用回调函数
#2.当对象被回收时，weakref.ref()对象会自动被回收，但
