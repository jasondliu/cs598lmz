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
#[<weakref at 0x000002A8F8C9E948; to 'A' at 0x000002A8F8C9E8D0>, ['']]
#[<weakref at 0x000002A8F8C9E948; dead>, ['']]
#[<weakref at 0x000002A8F8C9E948; dead>, []]
#[]

#结论：
#1.当a被删除时，a.c引用a，a不会被回收，所以a.c也不会被回收
#2.当a.c被删除时，a被回收，a.c也被回收
#3.当a.c被
