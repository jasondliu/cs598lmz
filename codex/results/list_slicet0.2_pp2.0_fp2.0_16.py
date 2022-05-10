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
#[<weakref at 0x000002B3B6B2C638; to 'A' at 0x000002B3B6B2C5C0>, []]
#这里的结果是因为a.c=a，所以a的引用计数为2，所以当del a时，a的引用计数为1，所以不会被回收，所以lst不会被删除

#第二个例子：
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
keepali0e.append(weakref.ref(a,callback))
del a

