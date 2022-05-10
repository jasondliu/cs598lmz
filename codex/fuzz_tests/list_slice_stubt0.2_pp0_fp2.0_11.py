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
del keepalive
print lst

#[str(), <weakref at 0x7f9b8b8c0c78; to 'A' at 0x7f9b8b8c0c90>]

#[str()]

#[str(), <weakref at 0x7f9b8b8c0c78; dead>]

#[str(), <weakref at 0x7f9b8b8c0c78; to 'A' at 0x7f9b8b8c0c90>]

#[str(), <weakref at 0x7f9b8b8c0c78; dead>]

#[str(), <weakref at 0x7f9b8b8c0c78; dead>]

#[str(), <weakref at 0x7f9b8b8c0c78; dead>]

#[str(), <weakref at 0x7f9b8b8c0c
