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
print(lst)

#[str(), <weakref at 0x7f4b4c0e6c18; to 'A' at 0x7f4b4c0e6c50>]

#[str()]

#[str(), <weakref at 0x7f4b4c0e6c18; dead>]

#[str(), <weakref at 0x7f4b4c0e6c18; dead>]

#[str(), <weakref at 0x7f4b4c0e6c18; dead>]

#[str(), <weakref at 0x7f4b4c0e6c18; dead>]

#[str(), <weakref at 0x7f4b4c0e6c18; dead>]

#[str(), <weakref at 0x7f4b4c0e6c18; dead>]

#[str(), <weakref at 0x7f4b
