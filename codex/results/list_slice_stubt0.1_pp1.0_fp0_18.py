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

#[str(), <weakref at 0x7f5d9c0a7f28; to 'A' at 0x7f5d9c0a7f10>]
#[<__main__.A object at 0x7f5d9c0a7f10>]

#[str(), <weakref at 0x7f5d9c0a7f28; dead>]
#[<__main__.A object at 0x7f5d9c0a7f10>]

#[str()]
#[<__main__.A object at 0x7f5d9c0a7f10>]

#[str()]
#[<__main__.A object at 0x7f5d9c0a7f10>]

#[str()]
#[<__main__.A object at 0x7f5d9c0a7f10>]

#[
