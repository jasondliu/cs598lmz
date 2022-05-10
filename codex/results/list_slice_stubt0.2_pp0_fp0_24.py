import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
del a
lst[0]=weakref.ref(lst[1],callback)
print(lst)
del lst
print(keepalive)

#[<weakref at 0x000002A7C5B9C0C8; to 'list' at 0x000002A7C5B9C1C8>, <__main__.A object at 0x000002A7C5B9C1D0>]
#[<__main__.A object at 0x000002A7C5B9C1D0>]

#[<weakref at 0x000002A7C5B9C0C8; dead>, <__main__.A object at 0x000002A7C5B9C1D0>]
#[<__main__.A object at 0x000002A7C5B9C1D0>]

#[<__main__.A object at 0x000002A7C5B9C1D0>]
#[<__main__
