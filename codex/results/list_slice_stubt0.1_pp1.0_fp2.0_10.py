import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
del a
print(lst)

#结果：
#[str(), <weakref at 0x000002A9F9D9C948; to 'A' at 0x000002A9F9D9C898>]
#这个结果说明，当a被删除时，a的弱引用被删除，但是a的引用计数不为0，因为a.c=a，所以a的引用计数为2，所以a不会被回收。
#如果a.c=None，则a的引用计数为1，a会被回
