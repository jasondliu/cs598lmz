import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print(lst)
print(keepali0e)
keepali0e[0]=None
print(lst)
print(keepali0e)

#['']
#[<weakref at 0x7f6c9c1b8c88; to 'A' at 0x7f6c9c1b8b00>]
#[]
#[None]

#['']
#[<weakref at 0x7f6c9c1b8c88; to 'A' at 0x7f6c9c1b8b00>]
#[]
#[None]

#['']
#[<weakref at 0x7f6c9c1b8c88; to 'A' at 0x7f6c9c1b8b00>]
#[]
#[None]

#['']
#[<weakref at 0x7f6c9c1b8c88; to 'A' at 0x7f6c9c1b8b00>]
#[]
