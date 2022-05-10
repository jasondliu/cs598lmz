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
del keepalive
print lst

#[str(), <weakref at 0x00000000024D8F88; to 'A' at 0x00000000024D8E48>]
#[<__main__.A object at 0x00000000024D8E48>]
#[str()]
