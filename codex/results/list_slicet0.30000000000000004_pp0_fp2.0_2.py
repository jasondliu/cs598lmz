import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
print(keepali0e)

#Output:
#[<weakref at 0x10f5e5b90; dead>, [''], <weakref at 0x10f5e5b90; dead>, [''], <weakref at 0x10f5e5b90; dead>, [''], <weakref at 0x10f5e5b90; dead>, [''], <weakref at 0x10f5e5b90; dead>, [''], <weakref at 0x10f5e5b90; dead>, [''], <weakref at 0x10f5e5b90; dead>, [''], <weakref at 0x10f5e5b90; dead>, [''], <weakref at 0x10f5e5b90; dead>, [''], <weakref at 0x10f5e5b90; dead>, [''], <weakref at 0x10f5e5b90; dead>, [''], <weakref at 0x10f5e5b90; dead>, [''], <weakref at 0x10f5e5
