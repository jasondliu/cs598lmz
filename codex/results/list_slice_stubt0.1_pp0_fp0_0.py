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

#[str(), <weakref at 0x7f8a7c0; to 'A' at 0x7f8a7b0>]
#[<__main__.A object at 0x7f8a7b0>]

#[str(), <weakref at 0x7f8a7c0; dead>]
#[<__main__.A object at 0x7f8a7b0>]

#[str()]
#[<__main__.A object at 0x7f8a7b0>]

#[str()]
#[]

#[str()]
#[]
