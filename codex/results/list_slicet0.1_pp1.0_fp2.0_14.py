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
#[<weakref at 0x000002A9A9D9F948; to 'A' at 0x000002A9A9D9F898>, ['']]
#[<weakref at 0x000002A9A9D9F948; dead>, ['']]
#[<weakref at 0x000002A9A9D9F948; dead>, []]
#[]
#[]

#结论：
#1.当对象被回收时，weakref.ref对象的callback函数会被调用，并且weakref.ref对象的状态会变为dead
#2.当weakref.ref对象的callback函数被调用时，weakref.ref对象的
