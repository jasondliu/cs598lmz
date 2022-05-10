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

#输出：
#[<weakref at 0x00000000026A5C48; to 'A' at 0x00000000026A5B70>, ['']]
#[<weakref at 0x00000000026A5C48; dead>, []]
#[<weakref at 0x00000000026A5C48; dead>, []]
#[<weakref at 0x00000000026A5C48; dead>, []]
#[<weakref at 0x00000000026A5C48; dead>, []]
#[<weakref at 0x00000000026A5C48; dead>, []]
#[<weakref at 0x00000000026A5C48; dead>, []]
#[<weakref at 0x00000000026A5C48; dead>, []]
#[<weakref at 0x00000000026A5C48; dead>, []]
#[<weakref at 0x00000000026A5C48; dead>, []]
#[<weakref at 0x00000000026
