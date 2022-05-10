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
#[<weakref at 0x00000000024E9C88; dead>, ['']]
#这个结果说明，循环引用的对象，在引用计数为0时，不会被回收，因为它还有一个弱引用，所以它是dead状态。
#当弱引用被回收时，它的回调函数callback会被调用，callback函数会删除lst中的一个元素，这样lst就不再是空的，
#这样while循环
