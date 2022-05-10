import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst[0]=weakref.ref(a,callback)
del a
print(lst)

#结果：[<weakref at 0x000002A7C2A2D7C8; to 'A' at 0x000002A7C2A2D748>]
#为什么会是这样？

#垃圾回收机制，垃圾回收机制只会回收引用计数为0的对象，但是当前的a对象的引用计数为1，因为它有一个循环引用，所以不会被回收，
#当a对象被回收的
