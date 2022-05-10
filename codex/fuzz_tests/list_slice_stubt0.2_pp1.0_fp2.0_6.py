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

#[str(), <__main__.A object at 0x7f8a8c0e5f10>, <weakref at 0x7f8a8c0e5d90; to 'A' at 0x7f8a8c0e5f10>]

#[str(), <__main__.A object at 0x7f8a8c0e5f10>, <weakref at 0x7f8a8c0e5d90; dead>]

#[str(), <__main__.A object at 0x7f8a8c0e5f10>, <weakref at 0x7f8a8c0e5d90; dead>]

#[str(), <__main__.A object at 0x7f8a8c0e5f10>, <weakref at 0x7f8a8c0e5d90; dead>]

#[str(), <
