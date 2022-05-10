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

#[str(), <weakref at 0x000001E6A5E8A8C8; to 'A' at 0x000001E6A5E8A898>]
#[str(), <weakref at 0x000001E6A5E8A8C8; dead>]
#[str()]

#weakref.ref(a,callback)返回一个弱引用对象，它指向a，当a被回收时，会调用callback函数。
#当a被回收时，lst中的弱引用对象会被自动清除，所以lst中的弱引用对象会
