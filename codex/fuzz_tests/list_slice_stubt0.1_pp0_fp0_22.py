import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
print(lst)
del a
print(lst)

#[str(), <weakref at 0x7f8c8c0f7e08; to 'A' at 0x7f8c8c0f7d68>]
#[str()]

#weakref.ref(obj,callback)
#创建一个弱引用，当obj被垃圾回收时，调用callback函数
#callback函数的参数是一个弱引用对象
#callback函数可以是None，这时候不会调用任何函数
#callback函数可以是一个可调用对象，这时候会
