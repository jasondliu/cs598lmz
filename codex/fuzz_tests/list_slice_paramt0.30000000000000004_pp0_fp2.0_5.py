import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
print lst
print keepali0e

#结果：
#['1']
#[<weakref at 0x00000000024B8B08; dead>, <weakref at 0x00000000024B8B38; dead>]

#解释：
#对象a的弱引用被删除了，但是对象a.c的弱引用没有被删除，因为对象a.c的弱引用是对象a的弱引用的一个别名，因此对象a的弱引用没有被删除，对象a.c的弱引用也
