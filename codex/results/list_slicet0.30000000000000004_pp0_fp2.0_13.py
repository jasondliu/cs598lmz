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
#[<weakref at 0x0000000002A9B818; dead>, []]
#可以看到，a对象的弱引用已经被回收，因此lst的第一个元素被删除
#这里的keepalive是一个列表，里面的元素是弱引用对象，而不是弱引用对象的引用

#结论：
#1.当一个对象的弱引用被回收时，它的回调函数会被调用。
#2.回调函
