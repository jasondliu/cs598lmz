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

#结果：
#[str(), <weakref at 0x000002A4E8F8C948; to 'A' at 0x000002A4E8F8C898>]
#[str()]

#结论：
#当弱引用对象被回收时，会调用回调函数，回调函数的参数是弱引用对象本身。
#回调函数的返回值会被忽略。
#回调函数的调用时机是不确定的，可能是在对
