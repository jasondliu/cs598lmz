import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
lst.append(weakref.ref(a,callback))
del a
print(lst)

#[str(), <weakref at 0x7f3b2c2d7e18; to 'A' at 0x7f3b2c2d7d68>, <weakref at 0x7f3b2c2d7e48; to 'A' at 0x7f3b2c2d7d68>]
#[str()]
#[str()]
#[str()]
#[str()]
#[str()]
#[str()]
#[str()]
#[str()]
#[str()]
#[str()]
#[str()]
#[str()]
#[str()]
#[str()]
#[str()]
#[str()]
#[str()]
#[str()]
#[str()]
#[str()]
#[str()]

