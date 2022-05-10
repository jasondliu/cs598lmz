import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
del a
print lst
print keepalive

#[str(), <weakref at 0x7f8c8c0e0c88; to 'A' at 0x7f8c8c0e0c50>]
#[<__main__.A object at 0x7f8c8c0e0c50>]

# 可以看到，当a被删除时，lst中的弱引用被自动删除，但是a的循环引用导致a不能被回收，所以keepalive中的a还存在。

# 如果把keepalive中的a删除，则a会被回收，l
