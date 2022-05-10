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

#[str(), <weakref at 0x7f8c8c0b0a98; to 'A' at 0x7f8c8c0b0b10>]
#[<__main__.A object at 0x7f8c8c0b0b10>]

#第一次打印lst，可以看到lst中有两个元素，一个是字符串，另一个是弱引用对象。
#第二次打印keepalive，可以看到keepalive中有一个A对象。
#第三次打印lst，可以看到lst中只
