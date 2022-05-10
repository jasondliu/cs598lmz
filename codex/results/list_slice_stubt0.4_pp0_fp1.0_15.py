import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst[0]=weakref.ref(a,callback)
print(lst)
print(keepalive)
del a
print(lst)
print(keepalive)
del keepalive[0]
print(lst)
print(keepalive)

#[<weakref at 0x00B0C6F8; to 'A' at 0x00B0C6E0>]
#[<__main__.A object at 0x00B0C6D0>]
#[<weakref at 0x00B0C6F8; dead>]
#[<__main__.A object at 0x00B0C6D0>]
#[]
#[]
