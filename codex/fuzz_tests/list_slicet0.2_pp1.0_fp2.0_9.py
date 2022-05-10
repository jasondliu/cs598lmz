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

#输出
#[<weakref at 0x00A0F7F8; to 'A' at 0x00A0F7E0>, []]
#说明：当a被删除时，a.c引用计数减1，但是a.c还是引用a，所以a的引用计数还是1，所以a不会被回收，
#因此a的弱引用不会被回收，所以lst不会被删除。

#3.
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append
