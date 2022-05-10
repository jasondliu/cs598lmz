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
del keepalive
print(lst)

#[<weakref at 0x000002C8F7D7F948; to 'A' at 0x000002C8F7D7F948>]
#[<weakref at 0x000002C8F7D7F948; dead>]

#第一个输出表明，弱引用a被创建，并且它指向a。
#第二个输出表明，当keepalive被删除时，a被回收，并且回调函数被调用，删除了lst中的弱引用。


