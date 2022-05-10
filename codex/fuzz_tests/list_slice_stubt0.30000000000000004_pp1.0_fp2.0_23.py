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

#[str(), <weakref at 0x7f7a7c0e5a98; to 'A' at 0x7f7a7c0e5a50>]
#[str(), <weakref at 0x7f7a7c0e5a98; dead>]

#可以看到，当a被回收时，lst中的weakref对象会变成dead状态，并且调用callback函数
#这里的callback函数是del lst[0]，所以lst中的str对象也会被删除
#所以lst最后只剩下一个dead的weakref对象
#当然
