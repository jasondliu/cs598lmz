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

#[str(), <weakref at 0x7f8f9c0a8e28; to 'A' at 0x7f8f9c0a8d68>]
#[str()]

#weakref.ref(a,callback)
#<weakref at 0x7f8f9c0a8e28; to 'A' at 0x7f8f9c0a8d68>
#a.c
#<__main__.A at 0x7f8f9c0a8d68>
#a.c.c
#<__main__.A at 0x7f8f9c0a8d68>
#a.c.c.c
#<__main__.A at 0x7f8f9c0a8d68>
#a.c.c.c.c
#<__main__.A at 0x7f8f9c0a8d68>
