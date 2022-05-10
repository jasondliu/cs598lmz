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
#[<weakref at 0x000002C8A8A8E908; to 'A' at 0x000002C8A8A8E8D0>, ['']]
#[<weakref at 0x000002C8A8A8E908; dead>, ['']]
#[<weakref at 0x000002C8A8A8E908; dead>, []]

#结论：
#弱引用的回调函数在引用的对象被回收时被调用
#弱引用的回调函数在引用的对象被回收时被调用
#弱引用的回调函数在引用的对象
