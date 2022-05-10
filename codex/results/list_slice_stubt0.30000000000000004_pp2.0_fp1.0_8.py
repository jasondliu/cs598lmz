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

#[str(), <weakref at 0x00000000040B8E08; to 'A' at 0x00000000040B8E48>]
#[<__main__.A object at 0x00000000040B8E48>]
