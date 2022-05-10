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
print lst
print keepalive

#[str(), <weakref at 0x7f9d9c0e4f78; to 'A' at 0x7f9d9c0e4f98>]
#[<__main__.A object at 0x7f9d9c0e4f98>]

#这里的第二个元素是一个弱引用，它引用的对象是一个循环引用，所以这个对象不会被回收。
#但是，当这个弱引用被回收时，它的回调函数会被调用，回调函
