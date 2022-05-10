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
#[str(), <weakref at 0x000002A9D9E9D948; to 'A' at 0x000002A9D9E9D898>]
#[str()]

#结论：
#当弱引用对象被回收时，回调函数会被调用，回调函数的参数是弱引用对象本身，
#回调函数的返回值会被忽略。

#回调函数的调用时机：
#当弱引用对
