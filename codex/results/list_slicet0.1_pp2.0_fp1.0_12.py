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
#[<weakref at 0x000002A8C8C7A948; to 'A' at 0x000002A8C8C7A898>, []]
#[<weakref at 0x000002A8C8C7A948; dead>, []]
#[<weakref at 0x000002A8C8C7A948; dead>, []]
#[<weakref at 0x000002A8C8C7A948; dead>, []]
#[<weakref at 0x000002A8C8C7A948; dead>, []]
#[<weakref at 0x000002A8C8C7A948; dead>, []]
#[<weakref at 0x000002A8C8C7A948; dead>, []]
#[<weakref at 0x000002A8C8C7A948; dead>, []]
#[<weakref at 0x000002A8C8C7A
