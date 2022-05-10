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
#[str(), <weakref at 0x000002B3C8F8D948; to 'A' at 0x000002B3C8F8D898>]

#结论：
#1.当对象被回收时，会调用回调函数，并将对象的弱引用从列表中删除
#2.当对象被回收时，会调用回调函数，并将对象的弱引用从列表中删除
#3.当对象被回
