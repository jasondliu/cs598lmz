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

#输出：
#[str(), <weakref at 0x00000000027F6D88; to 'A' at 0x00000000027F6D68>]
#[str()]

#第一次打印，lst中有两个元素，第一个是字符串，第二个是弱引用对象。
#第二次打印，lst中只有一个元素，因为弱引用对象被回调函数删除了。

#弱引用对象的回调函数，在
