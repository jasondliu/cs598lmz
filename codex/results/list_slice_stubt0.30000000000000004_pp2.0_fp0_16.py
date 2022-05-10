import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
lst.append(weakref.ref(a,callback))
del a
print lst

#[str(), <__main__.A object at 0x7f7c8b8a7b90>, <weakref at 0x7f7c8b8a7c10; to 'A' at 0x7f7c8b8a7b90>]

#这个例子中，a对象的引用计数为2，一个是lst中的引用，一个是a.c中的引用。
#当a对象被删除时，引用计数减少到1，因此a对象并没有被销毁。
#当a.c对象被删
