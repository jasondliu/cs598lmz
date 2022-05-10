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
#[<weakref at 0x000002A8A0B7B948; to 'A' at 0x000002A8A0B7B908>, ['']]
#[<weakref at 0x000002A8A0B7B948; dead>, ['']]
#[<weakref at 0x000002A8A0B7B948; dead>, []]
#[]

#结论：
#1.当对象被回收时，weakref会被自动删除
#2.当对象被回收时，weakref的回调函数会被自动调用
#3.当对象被回收时，weakref的回调函
