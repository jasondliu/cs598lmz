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
print(lst)
print(keepalive)

#结果：
#[str(), <weakref at 0x000002A8F9F9D948; to 'A' at 0x000002A8F9F9D908>]
#[<__main__.A object at 0x000002A8F9F9D908>]

#结论：
#当a被删除时，a的弱引用被删除，但是a的引用计数不为0，因为a.c=a，所以a的引用计数为1，所以a不会被回收。
#当a的引用计数
