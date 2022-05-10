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
#[<weakref at 0x000002A2E8D8F948; to 'A' at 0x000002A2E8D8F908>, ['']]
#[<weakref at 0x000002A2E8D8F948; dead>, ['']]
#[<weakref at 0x000002A2E8D8F948; dead>, []]

#结论：
#当对象被回收时，会调用回调函数，并且回调函数会在对象被回收之前被调用。
#回调函数的参数是弱引用对象，当对象被回收
