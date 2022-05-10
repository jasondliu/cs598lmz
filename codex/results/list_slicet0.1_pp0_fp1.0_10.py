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
#[<weakref at 0x000001E8B8D8C9C8; to 'A' at 0x000001E8B8D8C948>, []]
#这里的结果是因为，在删除a的时候，a的引用计数变为0，但是a.c还是指向a，所以a的引用计数变为1，所以a没有被回收。
#所以，在这里，a的引用计数变为0，a被回收，a.c也被回收，所以a.c的引
