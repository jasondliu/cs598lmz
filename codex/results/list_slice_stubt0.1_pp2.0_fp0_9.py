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
#[str(), <weakref at 0x000002A2D8A0A848; to 'A' at 0x000002A2D8A0A7F0>]
#[str()]

#结论：
#当弱引用对象被回收时，会调用回调函数，回调函数的参数是弱引用对象本身。
#回调函数的返回值会被忽略。
#回调函数会在对象被回收时调用，但是
