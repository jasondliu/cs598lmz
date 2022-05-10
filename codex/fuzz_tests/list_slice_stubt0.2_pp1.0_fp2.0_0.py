import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
lst[0]=a
lst[0]=weakref.ref(a,callback)
del a
print lst

#output:
#[<weakref at 0x7f7a0c0c9b88; to 'A' at 0x7f7a0c0c9b50>]
#[<weakref at 0x7f7a0c0c9b88; dead>]
#[<weakref at 0x7f7a0c0c9b88; dead>]
#[<weakref at 0x7f7a0c0c9b88; dead>]
#[<weakref at 0x7f7a0c0c9b88; dead>]
#[<weakref at 0x7f7a0c0c9b88; dead>]
#[<weakref at 0x7f7a0c0c9b88; dead>]
#[<weakref at 0x7f7a0c0c9b88; dead>]
#[<weakref at 0
