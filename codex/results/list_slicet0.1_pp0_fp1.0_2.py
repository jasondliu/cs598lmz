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
#[<weakref at 0x000002A9A8E0A948; to 'A' at 0x000002A9A8E0A898>, ['']]
#[<weakref at 0x000002A9A8E0A948; dead>, ['']]
#[<weakref at 0x000002A9A8E0A948; dead>, []]
#[]

#结论：
#1.当对象被回收时，weakref.ref对象会被自动回收，并且调用回调函数
#2.当对象被回收时，weakref.ref对象会被自动回收，并且
