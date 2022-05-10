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

#[<weakref at 0x000002B7C6E0B9B8; to 'str' at 0x000002B7C6E0B9A8>, []]

#结论：
#当引用计数为0时，会调用回调函数，并且回调函数会在调用前删除弱引用对象，
#所以回调函数中的引用计数为0的对象不会被回收，因为回调函数中的引用计数为0的对象
#还有一个弱引用对象指向
