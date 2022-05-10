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

#结果
#[<weakref at 0x000002A3E3C8D9C8; to 'str' at 0x000002A3E3C8D9A8>, []]
