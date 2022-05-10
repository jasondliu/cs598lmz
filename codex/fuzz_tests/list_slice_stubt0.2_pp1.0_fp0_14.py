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
#[str(), <weakref at 0x000002A8D8C9B948; to 'A' at 0x000002A8D8C9B8D0>]
#[str(), None]

#结论：
#当对象被删除时，回调函数会被调用，并且会把弱引用对象从列表中删除

#结论：
#当对象被删除时，回调函数会被调用，并且会把弱引用
