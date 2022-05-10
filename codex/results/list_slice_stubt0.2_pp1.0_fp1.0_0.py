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

#[str(), <weakref at 0x0000000003B9F948; to 'A' at 0x0000000003B9F908>]
#[<__main__.A object at 0x0000000003B9F908>]

#第一个元素是字符串，第二个元素是弱引用，指向A对象。
#当A对象被回收时，弱引用会被自动删除，回调函数callback会被调用，删除lst中的第一个元素。
#但是，由
