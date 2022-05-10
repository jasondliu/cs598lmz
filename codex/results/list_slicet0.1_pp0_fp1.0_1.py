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
#[<weakref at 0x000002A9E0B8D948; to 'A' at 0x000002A9E0B8D908>, ['']]
#[<weakref at 0x000002A9E0B8D948; dead>, ['']]
#[<weakref at 0x000002A9E0B8D948; dead>, []]
#[]

#结论：
#1.当对象被回收时，弱引用对象的状态会变为dead
#2.当对象被回收时，回调函数会被调用
#3.回调函数可以改变对象的状态
