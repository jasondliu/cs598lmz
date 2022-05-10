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
print keepali0e

#结果：
#[<weakref at 0x00000000025B9B08; dead>, ['']]
#这个结果说明，当对象a被删除后，a.c的引用计数减少，但是a.c的引用计数不为0，所以a.c不会被回收，
#而且a.c的引用计数为1，所以a.c不会被回收，而且a.c的引用计数为1，所以a.c不会被回收，而且a.c的引用计数为1
