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
print keepali0e

#python2.7.10
#[<weakref at 0x7f7d6c0b6d88; to 'A' at 0x7f7d6c0b6d68>, ['']]
#python3.5.2
#[<weakref at 0x7f7d6c0b6d88; to 'A' at 0x7f7d6c0b6d68>, ['']]

#python2.7.10
#[<weakref at 0x7f7d6c0b6d88; to 'A' at 0x7f7d6c0b6d68>, ['']]
#python3.5.2
#[<weakref at 0x7f7d6c0b6d88; to 'A' at 0x7f7d6c0b6d68>, ['']]

#python2.7.10
#[<weakref at 0x7f7d6c0b6d88; to 'A' at 0x7f7d6c
