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

#[str(), <weakref at 0x7f8e7c0b9e18; to 'A' at 0x7f8e7c0b9e10>]
#[<__main__.A object at 0x7f8e7c0b9e10>]

#[str(), <weakref at 0x7f8e7c0b9e18; dead>]
#[<__main__.A object at 0x7f8e7c0b9e10>]

#[str()]
#[<__main__.A object at 0x7f8e7c0b9e10>]

#[str()]
#[<__main__.A object at 0x7f8e7c0b9e10>]

#[str()]
#[<__main__.A object at 0x7f8e7c0b9e10>]

#[
