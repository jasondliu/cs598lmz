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

#[str(), <weakref at 0x7f7a9c0; to 'A' at 0x7f7a9b0>]
#[<__main__.A object at 0x7f7a9b0>]

#第二个例子
import weakref
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
del a
print lst
print keepalive

#[str(), <weakref at 0x7f7a9c0; to 'A' at 0x7f7a9b0>]
#[<__main__.A object at 0x7f7a9b0>]

#第三个
