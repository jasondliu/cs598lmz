import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
a.a=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
del a
print lst
print keepalive

#结果：
#[str(), <weakref at 0x00000000029E7F48; to 'A' at 0x00000000029E7E48>]
#[<__main__.A object at 0x00000000029E7E48>]
#结论：
#当弱引用指向的对象被回收时，调用回调函数，并且删除弱引用，但是弱引用指向的对象不会被回收
#当弱引用指向的对象被回收
