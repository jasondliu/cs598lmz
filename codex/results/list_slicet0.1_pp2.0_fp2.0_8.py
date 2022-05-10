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
#[<weakref at 0x000002A6E8C6E948; to 'A' at 0x000002A6E8C6E898>, []]
#这个结果说明，当a被删除时，a.c也被删除了，因为a.c指向a，所以a.c也被删除了。
#这个结果说明，当a被删除时，a.c也被删除了，因为a.c指向a，所以a.c也被删除了。
#这个结果说
