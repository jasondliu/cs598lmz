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

#输出：
#[<weakref at 0x00A6D1F0; dead>, <weakref at 0x00A6D1F8; dead>, []]

#第二种情况：
#示例3：
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

#输出：
#[<weakref at 0x00A6D1F0; dead>, <weakref at 0x00A6D1F8; dead>, []]

#第三种情况：
#示例4：
import weak
