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
#[<weakref at 0x000001F9F9D9B948; to 'A' at 0x000001F9F9D9B898>, []]
#[<weakref at 0x000001F9F9D9B948; dead>, []]
#[<weakref at 0x000001F9F9D9B948; dead>, []]
#[<weakref at 0x000001F9F9D9B948; dead>, []]
#[<weakref at 0x000001F9F9D9B948; dead>, []]
#[<weakref at 0x000001F9F9D9B948; dead>, []]
#[<weakref at 0x000001F9F9D9B948; dead>, []]
#[<weakref at 0x000001F9F9D9B948; dead>, []]
#[<weakref at 0x000001F9F9D9B
