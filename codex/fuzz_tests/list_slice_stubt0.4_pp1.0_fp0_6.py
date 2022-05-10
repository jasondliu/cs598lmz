import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
print(lst)
del a
print(lst)
print(lst[0])
print(lst[1]())
print(lst)
print(lst[0])
print(lst[1]())
print(lst)
print(lst[0])
print(lst[1]())
print(lst)

#[str(), <weakref at 0x10d28d948; to 'A' at 0x10d28d8d0>]
#[str(), <weakref at 0x10d28d948; dead>]
#
#<__main__.A object at 0x10d28d8d0>
#[str(), <weakref at 0x10d28d948; to 'A' at 0x10d28d8d0>]
#
#<__main__.A object at 0x10d28d8d0>
#[str(), <weakref at 0x10d28d9
