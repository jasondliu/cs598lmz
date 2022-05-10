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

#结果是：
#[[<weakref at 0x7f5f0c1a5a40; to 'A' at 0x7f5f0c1a5a50>, ['\x00']],
#[<weakref at 0x7f5f0c1a5a40; dead>, ['\x00']],
#[<weakref at 0x7f5f0c1a5a40; dead>, []]]

#第一个元素是：<weakref at 0x7f5f0c1a5a40; to 'A' at 0x7f5f0c1a5a50>
#说明a被回收了，但是a.c还没有被回收，因为a.c指向a，a没有被回收，a.c
