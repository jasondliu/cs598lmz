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

#结果：
#[<weakref at 0x00000000023A9E88; to 'A' at 0x00000000023A9E48>, []]
#这个结果说明，当a被删除的时候，a.c的引用计数为1，所以a.c不会被删除，而a.c的引用计数为1，是因为a.c指向了a，而a还没有被删除，所以a.c的引用计数为1，所以a.c不会被删除，而a.c的引用计数为1
