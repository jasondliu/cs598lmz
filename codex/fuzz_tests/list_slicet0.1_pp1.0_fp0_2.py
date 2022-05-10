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
#[<weakref at 0x000002A9F8E8B948; to 'A' at 0x000002A9F8E8B898>, ['']]
#[<weakref at 0x000002A9F8E8B948; dead>, ['']]
#[<weakref at 0x000002A9F8E8B948; dead>, []]
#[]

#结论：
#1.当对象被回收时，回调函数会被调用，并且回调函数的参数是对象的弱引用
#2.回调函数的参数是对象的弱引用，所以在回调函数
