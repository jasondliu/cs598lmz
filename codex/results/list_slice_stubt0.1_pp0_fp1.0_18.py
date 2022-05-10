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
del keepalive
print lst

#[str(), <__main__.A object at 0x7f8a8c0e7a10>, <weakref at 0x7f8a8c0e7a40; to 'A' at 0x7f8a8c0e7a10>]

#[str(), <__main__.A object at 0x7f8a8c0e7a10>, <weakref at 0x7f8a8c0e7a40; dead>]

#[str(), <weakref at 0x7f8a8c0e7a40; dead>]

#[str()]

#[]

#[]

#[]

#[]

#[]

#[]

#[]

#[]

#[]

#[]

#[]

#[]

#[]

#[]

#[]

#[]

