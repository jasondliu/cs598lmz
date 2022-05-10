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
#[<weakref at 0x000001E8C8F8D948; to 'A' at 0x000001E8C8F8D908>, []]
#这里的结果是因为a.c=a，导致a的引用计数为2，所以在del a的时候，引用计数为1，所以不会调用回调函数，所以lst中的元素不会被删除，所以while循环不会结束。
#如果a.c=None，则结果为：
#[<weakref at 0x000001E8C8
