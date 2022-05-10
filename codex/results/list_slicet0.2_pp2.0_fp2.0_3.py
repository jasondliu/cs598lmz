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
#[<weakref at 0x0000020E5E5A5C88; to 'A' at 0x0000020E5E5A5C48>, []]
#[<weakref at 0x0000020E5E5A5C88; dead>, []]
#[<weakref at 0x0000020E5E5A5C88; dead>, []]
#[<weakref at 0x0000020E5E5A5C88; dead>, []]
#[<weakref at 0x0000020E5E5A5C88; dead>, []]
#[<weakref at 0x0000020E5E5A5C88; dead>, []]
#[<weakref at 0x0000020E5E5A5C88; dead>, []]
#[<weakref at 0x0000020E5E5A5C88; dead>, []]
#[<weakref at 0x0000020E5E5A5C88; dead>, []]
#[
