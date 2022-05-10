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
#[<weakref at 0x000002A5C5E8D7C8; to 'A' at 0x000002A5C5E8D7B0>, ['']]
#[<weakref at 0x000002A5C5E8D7C8; dead>, ['']]
#[<weakref at 0x000002A5C5E8D7C8; dead>, []]
#[]

#结论：
#1.当对象被回收时，weakref.ref()对象的callback函数会被调用
#2.当对象被回收时，weakref.ref()对象的callback函数会被调用，但是callback函数中的对象已
