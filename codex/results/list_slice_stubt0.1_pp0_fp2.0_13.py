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

#[str(), <weakref at 0x7f8f8c0a9b48; to 'A' at 0x7f8f8c0a9b70>]
#[<__main__.A object at 0x7f8f8c0a9b70>]

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

#[str(), <weakref at 0x7f8f8c0a9b48; to 'A' at 0x7f8f8c0a9b70>]
#[<__main__.A object at
