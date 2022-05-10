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
print keepalive

#[str(), <__main__.A object at 0x7f7d8d6e2f10>, <weakref at 0x7f7d8d6e2f50; to 'A' at 0x7f7d8d6e2f10>]
#[<__main__.A object at 0x7f7d8d6e2f10>]

#这里的keepalive是一个列表，其中包含一个对象a的引用，而a又包含一个对象a的引用，这样就形成了一个循环引用，
#因此，a不会被回收
