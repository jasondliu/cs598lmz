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
#[<weakref at 0x000002C2E9C9F948; to 'A' at 0x000002C2E9C9F908>, []]
#这是因为当a被删除时，a.c被设置为None，因此a的弱引用被回调。
#但是，a.c仍然指向a，因此a不会被垃圾回收。
#因此，当我们尝试删除lst[0]时，它仍然存在，因此循环永远不会结束。
#这是一个循环引
