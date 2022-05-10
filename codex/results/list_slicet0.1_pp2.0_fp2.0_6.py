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
#[<weakref at 0x000002A8D3E1E948; to 'A' at 0x000002A8D3E1E908>, []]
#这里的结果是因为a.c=a，导致a的引用计数不为0，所以a不会被回收，所以callback不会被执行，所以lst不会被清空，所以while循环不会结束
#如果a.c=None，则结果为：
#[<weakref at 0x000002A8D3E1E948; dead>, []]
#这里的结果是
