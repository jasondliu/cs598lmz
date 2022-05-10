import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print lst
del a
print lst
lst=[]
a=A()
keepali0e.append(weakref.ref(a))
del a
print keepali0e
print keepali0e[0]() is None

#output
['']
[]
[<weakref at 0x0000000002A8B1C8; dead>, <weakref at 0x0000000002A8B108; dead>]
False
